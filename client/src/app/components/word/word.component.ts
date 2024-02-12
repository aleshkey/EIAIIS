import {Component, OnInit} from '@angular/core';
import {Word} from "../../model/Word";
import {WordService} from "../../service/word.service";
import {ActivatedRoute, Router} from "@angular/router";
import {FormControl, FormsModule, ReactiveFormsModule} from "@angular/forms";
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatSelectModule} from "@angular/material/select";
import {MatInputModule} from "@angular/material/input";
import {MatCheckbox} from "@angular/material/checkbox";
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Constants} from "../../Constants";


@Component({
  selector: 'app-word',
  templateUrl: './word.component.html',
  styleUrls: ['./word.component.css'],
  })

export class WordComponent implements OnInit {
  word!: Word;
  disableSelect = new FormControl(false);
  states:Record<string, any> = {};



  constructor(
    private http: HttpClient,
    private wordService: WordService,
    private route: ActivatedRoute,
    public router: Router
  )
  {

  }





  ngOnInit(): void {
    this.states = this.wordService.getStates();
    let id = this.route.snapshot.paramMap.get('id');
    while (id==null);
    this.wordService.getOne(parseInt(id)).subscribe(word=>{
      this.word = word
    });
    console.log(this.word)
  }

  sendData(): void{
    const formsData = this.word.forms.map(form => {
    return {
      word_id: this.word.id,
      form: form.word,
      number: form.number,
      gender: form.gender,
      case: form.case,
      pos: form.part_of_speech,
      animacy: form.animation,
      tense: form.time,
      aspect: form.type,
      mood: form.inclination,
      };
    });

    let id = this.route.snapshot.paramMap.get('id');
    while (id==null);

    this.http.post(Constants.WORDS_API, formsData).subscribe();
  }
}
