function PopupQueue() {
    this.items = [];
}

PopupQueue.prototype.isEmpty = function() {
    return this.items.length === 0;
};

PopupQueue.prototype.enqueue = function(id) {
    this.items.push(id);
};

PopupQueue.prototype.dequeue = function() {
    return this.items.shift();
};

PopupQueue.prototype.next = function() {
    return this.items[0];
};

PopupQueue.prototype.isNext = function(id) {
    return this.next() === id;
};