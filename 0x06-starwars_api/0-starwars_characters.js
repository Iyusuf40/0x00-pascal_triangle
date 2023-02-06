#!/usr/bin/node

const filmId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/';
const filmsPath = 'films/';
const filmUrl = baseUrl + filmsPath + filmId;
const util = require('util');
const request = util.promisify(require('request'));

const map = {};

async function getPeople () {
  const res = await request(filmUrl);
  const characters = JSON.parse(res.body).characters;
  const AllPromises = await Promise.all(characters.map(function (val) {
    return request(val);
  }));
  AllPromises.map(function (val) {
    const jsonVal = JSON.parse(val.body);
    map[jsonVal.url] = jsonVal.name;
    return map;
  });
  characters.forEach(function (val) {
    console.log(map[val]);
  });
}

getPeople();
