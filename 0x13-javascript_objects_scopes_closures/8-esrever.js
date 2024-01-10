#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  let revList = [];
  list.forEach(element => {
    revList[--len] = element;
  });
  return revList;
};
