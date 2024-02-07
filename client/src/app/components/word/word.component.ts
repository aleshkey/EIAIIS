import {Component, OnInit} from '@angular/core';
import {Word} from "../../model/Word";
import {WordService} from "../../service/word.service";
import {ActivatedRoute, Router} from "@angular/router";


@Component({
  selector: 'app-word',
  templateUrl: './word.component.html',
  styleUrls: ['./word.component.css'] // исправлено на styleUrls
})
export class WordComponent implements OnInit {
  word!: Word;

  constructor(
    private wordService: WordService,
    private route: ActivatedRoute,
    public router: Router
  ) {}

  ngOnInit(): void {
    let id = this.route.snapshot.paramMap.get('id');
    while (id==null);
    this.wordService.getOne(parseInt(id)).subscribe(word=>{
      this.word = word
    });
    console.log(this.word)
  }
}
