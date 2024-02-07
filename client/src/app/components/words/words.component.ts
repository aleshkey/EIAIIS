import {Component, OnInit} from '@angular/core';
import {Word} from "../../model/Word";
import {WordService} from "../../service/word.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-words',
  templateUrl: './words.component.html',
  styleUrl: './words.component.css'
})
export class WordsComponent implements OnInit{

  words?: Word[];

  constructor(
    private wordService: WordService,
    public router: Router
  ) {}

  ngOnInit(): void {
    this.wordService.getAll().subscribe(
      data=>{
        this.words = data;
      }
    )
  }

}
