jQuery(window).on('elementor/frontend/init', function() {
    setTimeout(() => {
        // Elementor IDs
        popups = {
            uk: 2707,
            eu: 2710,
        };

        const controller = new PopupController();

        let url = 'https://pro.ip-api.com/json';

        const params = new URL(document.location).searchParams;

        const magic = params.get('magic_ip');

        if (magic) {
            url += '/' + magic;
        }

        const showPopups = async (data, status, xhr) => {
            if (data.countryCode === 'GB') {
                controller.showPopup(popups.uk);
            }

            if (data.continentCode === 'EU' && data.countryCode !== 'GB') {
                controller.showPopup(popups.eu);
            }

            // show IWC popup 8s after current popup is closed
            jQuery(document).on('elementor/popup/hide', (e, id) => {
                if (id === popups.uk || id === popups.eu) {
                    setTimeout(() => controller.showPopup(popups.iwc), 8000);
                }
            });

            jQuery(document).on('elementor/popup/hide', (e, id) => {
                if (id === popups.iwc) {
                    // TODO: manually trigger push woosh
                    Pushwoosh.subscribe();
                }
            });
        };

        jQuery.get(
            url, {
                key: 'joo1Uvji06yDxFg', // token
                fields: 'continentCode,countryCode',
            },
            showPopups
        );
    }, 1000);
});