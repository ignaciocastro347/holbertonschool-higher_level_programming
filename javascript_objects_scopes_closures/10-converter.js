#!/usr/bin/node

exports.converter = function (base) {
  return (num) => {
    const binary = num.toString(base);
    return parseInt(binary, base);
  };
};
