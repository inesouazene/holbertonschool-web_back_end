/* eslint-disable no-unused-vars */

class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  // Getter and Setter for code
  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = value;
  }

  // Getter and Setter for name
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // Method to display full currency
  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}

export default Currency;
