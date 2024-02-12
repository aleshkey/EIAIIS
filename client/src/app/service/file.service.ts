import { Injectable } from '@angular/core';
import {Constants} from "../Constants";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class FileService {

  constructor(private http: HttpClient) { }

  sendRequest(formData: FormData){
    console.log(2)
    return this.http.post(Constants.WORDS_API, formData)
  }
}
