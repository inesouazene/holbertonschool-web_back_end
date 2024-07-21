class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Method to cast class instance to a number
  valueOf() {
    return this._size;
  }

  // Method to cast class instance to a string
  toString() {
    return this._location;
  }
}

export default HolbertonClass;
