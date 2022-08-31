var showModalKyc = false;
var disableSubmit = false;
class KycWarningMessage {
	constructor() {
		this.message = $("#kyc_skrill_warning");
		this.checked = false;
	}
	hide() {
		this.message
			.removeClass("show-the-notification")
			.addClass("hide-the-notification");
	}
	show() {
		this.message
			.removeClass("hide-the-notification")
			.addClass("show-the-notification");
	}
	isActive() {
		return this.message.hasClass("show-the-notification");
	}
	isEnabled() {
		return this.message.length;
	}
	sendRequest(params) {
		return $.ajax({
			url: "/json/kyc_skrill_check.json",
			async: false,
			cache: false,
			type: "POST",
			data: params,
		});
	}
}
function getExRate(currency_from, currency_to) {
	var er_url = "/json/er.json";
	var key = "ifx_currency" + currency_from + currency_to;
	var rate = null;
	if (typeof sessionStorage != "undefined") {
		var rateStr = sessionStorage.getItem(key);
		if (rateStr !== null) {
			rate = JSON.parse(rateStr);
			if (rate[0] > 0 && Date.now() - rate[1] < 3600000) {
				return rate[0];
			}
		}
	}
	$.ajax({
		url: er_url,
		async: false,
		cache: false,
		type: "POST",
		data: { currency_from: currency_from, currency_to: currency_to },
		success: function (data) {
			if (data !== "") {
				rate = data;
				if (typeof sessionStorage != "undefined") {
					sessionStorage.setItem(key, JSON.stringify([rate, Date.now()]));
				}
			}
		},
	});
	return rate;
}
function getUsdEq(amount, currency) {
	if (currency === "USD") {
		return amount;
	}
	var rate = getExRate(currency, "USD");
	return amount * rate;
}
function KycData(jsonString) {
	this.ready = true;
	this.errorMessages = [];
	try {
		var obj = JSON.parse(jsonString);
	} catch (e) {
		this.errorMessages.push(e);
		obj = {};
	}
	var props = ["aggregatedAmount", "rules", "exceptAccounts", "auto"];
	props.forEach(function (prop) {
		if (!obj.hasOwnProperty(prop)) {
			this.ready = false;
			this.errorMessages.push("Parameter missing: " + prop);
		} else {
			this[prop] = obj[prop];
		}
	}, this);
}
function getKycCheckMessage() {
	var kycData = null;
	var url = "/json/kyc_check.json";
	$.ajax({
		url: url,
		async: false,
		cache: false,
		type: "POST",
		data: {},
		success: function (data) {
			kycData = new KycData(data);
		},
		error: function () {
			kycData = new KycData("{}");
		},
	});
	return kycData;
}
function amountChangeListener(ev, kycData) {
	showModalKyc = false;
	disableSubmit = false;
	var amount = 0;
	var amountInput = ev.target;
	if ($(amountInput).is("input")) {
		amount = parseInt($(amountInput).val());
	} else if ($(amountInput).is("select")) {
		amount = parseInt(amountInput.options[amountInput.selectedIndex].text);
	}
	var currency = $("[id^=currency]:visible").val();
	var usdAmount = getUsdEq(amount, currency);
	var totalAmount = usdAmount + kycData.aggregatedAmount;
	if (
		!(usdAmount > 0) ||
		!(amount > 0) ||
		!(totalAmount > 0) ||
		typeof currency !== "string"
	) {
		return;
	}
	if (
		(typeof isBankWire == "undefined" || !isBankWire) &&
		isAffiliateAccountExcludedFromKYCCheck(kycData)
	) {
		return;
	}
	for (var key in kycData.rules) {
		if (
			kycData.rules.hasOwnProperty(key) &&
			totalAmount >= kycData.rules[key].threshold
		) {
			if (kycData.rules[key].disableSubmit) {
				disableSubmit = true;
			}
			var upload_link = kycData.auto
				? kycPopupMessages["upload_link"]
				: kycPopupMessages["upload_link"] +
				  "?type=" +
				  kycData.rules[key].documentId;
			showModalKyc = true;
			prepareModal(
				kycPopupMessages[kycData.rules[key].message],
				upload_link,
				disableSubmit
			);
			break;
		}
	}
}
function isAffiliateAccountExcludedFromKYCCheck(kycData) {
	var tradingAccount = $("#account").val();
	return (
		kycData.hasOwnProperty("exceptAccounts") &&
		kycData.exceptAccounts.includes(tradingAccount)
	);
}
function prepareModal(message, link, disableSubmit) {
	$("#kycMessage").empty();
	$("#kycMessage").append("<p>" + message + "</p>");
	$("#kyc_upload_link").attr("href", link);
	$("#modal_redirect_btn").attr("href", link);
	if (disableSubmit) {
		$("#modal_submit_group").hide();
		$("#modal_redirect_btn").show();
		$("#upload_link_1").hide();
	} else {
		$("#modal_submit_group").show();
		$("#modal_redirect_btn").hide();
		$("#upload_link_1").show();
	}
}
jQuery(function () {
	$.urlParam = function (name) {
		var results = new RegExp("[?&]" + name + "=([^&#]*)").exec(
			window.location.href
		);
		if (results == null) {
			return null;
		} else {
			return results[1] || 0;
		}
	};
	if ($.urlParam("success") || $.urlParam("failure")) {
		return;
	}
	var kycData = getKycCheckMessage();
	if (!kycData.ready) {
		console.log(kycData.errorMessages);
		return;
	}
	var form = $("#paymentForm");
	if (form.length !== 1) {
		form = $("#withdrawForm");
	}
	if (form.length !== 1) {
		form = $("#withdrawalForm");
	}
	if (form.length !== 1) {
		console.log("The payment form was not found");
		return;
	}
	$(form).on("change", "[id*=amount]:visible:not(div)", function (e) {
		amountChangeListener(e, kycData);
	});
	$(form).on("keydown", "[id*=amount]:visible:not(div)", function (e) {
		var key = e.charCode ? e.charCode : e.keyCode ? e.keyCode : 0;
		if (key === 13) {
			$(e.currentTarget).change();
		}
	});
	$("#kycModal").on("click", "#modal_agree_btn", function (e) {
		form.trigger("submit");
	});
	$("#agree_checkbox").change(function () {
		$("#modal_agree_btn").attr("disabled", !this.checked);
	});
	var messageBoxHandler = new KycWarningMessage();
	var submitBtn = form.find(":submit");
	$(submitBtn)
		.on("click", function (e) {
			var values = form.serializeObject();
			var formIsValid = [true];
			if (form.prop("id") === "withdrawForm") {
				formIsValid = $(window.WithdrawForm.validate(values));
			} else if (form.prop("id") === "paymentForm") {
				formIsValid = $(window.paymentForm.validate(values));
			}
			if (showModalKyc && formIsValid[0] === true) {
				e.preventDefault();
				$("#kycModal").modal("show");
			}
		})
		.on("click", function (e) {
			if (!messageBoxHandler.isEnabled()) {
				return true;
			}
			if (messageBoxHandler.isActive()) {
				return true;
			}
			var values = form.serializeObject();
			messageBoxHandler.sendRequest(values).then(function (data) {
				if (data && data.hasOwnProperty("verified") && data.verified) {
					form.submit();
					return true;
				}
				messageBoxHandler.show();
			});
			e.preventDefault();
			e.stopImmediatePropagation();
		});
});
