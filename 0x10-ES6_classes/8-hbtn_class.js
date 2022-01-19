export default class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  set size(value) {
    this._size = value;
  }

  get size() {
    return this._size;
  }

  set location(value) {
    this._location = value;
  }

  get location() {
    return this._location;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'number') return this.size;
    if (hint === 'string') return this.location;
    return null;
  }
}
