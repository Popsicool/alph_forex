function PopupController() {
    this.lsPrefix = 'ifx-poup-'; // localStorage prefix

    this.queue = new PopupQueue();
}

PopupController.prototype.getPopup = function(id) {
    return window.elementorFrontend.documentsManager.documents[id];
};

PopupController.prototype.getChoice = function(id) {
    return localStorage.getItem(this.lsPrefix + id);
};

PopupController.prototype.saveChoice = function(id) {
    localStorage.setItem(this.lsPrefix + id, true);
};

PopupController.prototype.addCloseHook = function(id) {
    jQuery(document).on('elementor/popup/hide', (e, _id) => {
        if (id !== _id) {
            return;
        }

        if (this.queue.isNext(id)) {
            this.queue.dequeue();
        }

        this.saveChoice(id);

        if (!this.queue.isEmpty()) {
            this.showPopup(this.queue.next());
        }
    });
};

PopupController.prototype.showPopup = function(id) {
    if (this.getChoice(id)) {
        console.info('Already shown popup ' + id);
        return;
    }

    const popup = this.getPopup(id);

    if (popup === undefined) {
        console.warn('Failed to get popup ' + id);
        return;
    }

    popup.initModal(); // Elementor function

    this.queue.enqueue(id);

    this.addCloseHook(id);

    if (this.queue.isNext(id)) {
        popup.showModal(); // Elementor function
    }

    if (!this.queue.isNext(id)) {
        // check if another popup is currently in-progress
        // this (next) popup will be invoked by closeHook method
        console.warn('Another popup is in-progress ' + this.queue.next());
        console.warn(`Next (future) popup ${id} will shown be later`);
    }
};