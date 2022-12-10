#!/usr/bin/node

exports.esrever = function (list) {
  new_list = [];
  list.forEach(item => new_list.unshift(item));
  return new_list;
};
