import {Component, Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Word} from "../model/Word";
import {Constants} from "../Constants";
import {NONE_TYPE} from "@angular/compiler";

@Injectable({
  providedIn: 'root'
})
export class WordService {

  constructor(private http: HttpClient) { }

  getAll(){
    return this.http.get<Word[]>(Constants.WORDS_API);
  }

  getOne(id: number){
    return this.http.get<Word>(Constants.WORDS_API+"/"+id);
  }

  getStates(){
    return Constants.STATES
  }
}
