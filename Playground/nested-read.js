/*
Playground for me to efficiently make a function that will sparse out a value from an nested object within an array within an object in a Mongo document. Key doesn't matter because the value will be mapped to a different key before PUT Request to external app 

Input: Object
Output: Value ("String")
*/

"use strict";

const watch_list = {
    first_name: "Thaddius",
    last_name: "Testerville",
    movies: [
    {
        name: "Kill Jill II",
        release_date: "2000-01-27",
        director: "Quentin Terenbino",
        actors: ["Mac", "Fred", "Jeff"]
    },
    {
        name: "Poltervise",
        release_date: "1980-11-03",
        director: "Stephano Spielburg",
        actors: ["Lucy", "Fredirick"]
    },
    {
        name: "The Room",
        release_date: "1975-07-13",
        director: "",
        actors: ["Brain", "Helen", "Nixon", "Reagan"]
    },

],
   birth_date: "1998-07-31"
}

// Returns undefined because: TypeError: Cannot read property 'name' of undefined
function loopMethod (object) {
    const movies = object.movies;
    const returnVal = []
    for (const iterator of movies) {
        returnVal.push(movies[iterator].name)
    }
    return returnVal 
}

function reduceMethod (object, nested_object, value) { // Parameters: Object, String, String
    const returnVal = [] 
    for (let index = 0; index < object[nested_object].length; index++) {
        let path = [ nested_object, index, value]
        let result = path.reduce((a,v) => a[v], object)
        returnVal.push(result)
    }   
    return returnVal 
}

console.log("Hello World");
console.log("Watch List User:", watch_list.first_name + " " + watch_list.last_name, "\n");
console.log("Watch List Movies:", reduceMethod(watch_list, 'movies', 'name'), "\n");
console.log("Watch List Movies:", watch_list.movies.length, "\n");

