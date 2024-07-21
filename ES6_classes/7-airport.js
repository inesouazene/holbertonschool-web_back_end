class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Method to return the airport code
  toString() {
    return `[object ${this._code}]`;
  }
}

export default Airport;
