import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import * as http from "http";
import {Word} from "../model/Word";
import {Constants} from "../Constants";

@Injectable({
  providedIn: 'root'
})
export class PathService {

  constructor(private http: HttpClient) { }

  setPath(path: any){
    return this.http.post(Constants.PATH_API,{
      "path": path
    });
  }



}
