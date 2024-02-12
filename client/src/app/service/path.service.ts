import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import * as http from "http";
import {Word} from "../model/Word";
import {Constants} from "../Constants";
import {response} from "express";

@Injectable({
  providedIn: 'root'
})
export class PathService {

  constructor(private http: HttpClient) { }
  setPath(formData : any){
    return this.http.post("/path", formData);
  }

  sendRequest(formData: FormData){
    console.log(2)
    return this.http.post(Constants.PATH_API, formData)
  }


}
