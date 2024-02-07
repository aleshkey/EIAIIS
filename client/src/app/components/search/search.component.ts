import {Component, OnInit} from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormControl } from '@angular/forms';
import { debounceTime, distinctUntilChanged, switchMap } from 'rxjs/operators';
import { Observable } from 'rxjs';
import {Word} from "../../model/Word";
import {SearchService} from "../../service/search.service";

@Component({
  selector: 'search',
  templateUrl: './search.component.html',
})
export class SearchComponent implements OnInit{
  autocompleteOptions!: Word[];
  inputValue: string = '';

  constructor(private searchService: SearchService) {
  }

  search() {
    this.searchService.search(this.inputValue).subscribe(data => {
        console.log(data);
        this.autocompleteOptions = data
      }
    )
  }

  ngOnInit(): void {
    this.searchService.search(this.inputValue).subscribe(data => {
        console.log(data);
        this.autocompleteOptions = data
      }
    )
  }
}
