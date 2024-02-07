import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Constants} from "../Constants";
import {Word} from "../model/Word";

@Injectable({
  providedIn: 'root',
})
export class SearchService {

  constructor(private http: HttpClient) {}

  search(query: string) {
    const url = `${Constants.API_URL}/search?query=${query}`;
    return this.http.get<Word[]>(url);
  }
}
