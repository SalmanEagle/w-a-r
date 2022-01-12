pragma solidity ^0.8.11;

contract MyContract {
    string value;

    constructor() public {
        value = "myValue";
    }

    function get() public view returns (string) {
        return value;
    }

    function set(string _value) public {
        value = _value;
    }
}
