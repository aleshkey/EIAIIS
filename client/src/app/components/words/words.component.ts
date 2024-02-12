import {Component, OnInit} from '@angular/core';
import {Word} from "../../model/Word";
import {WordService} from "../../service/word.service";
import {Router} from "@angular/router";
import {HttpClient} from "@angular/common/http";
import { MatDialog } from '@angular/material/dialog';
import { ReportDialogComponent } from '../report-dialog/report-dialog.component';
import {Constants} from "../../Constants";

@Component({
  selector: 'app-words',
  templateUrl: './words.component.html',
  styleUrl: './words.component.css'
})
export class WordsComponent implements OnInit{

  words?: Word[];
  constructor(
    private wordService: WordService,
    public router: Router,
    private http: HttpClient,
    private dialog: MatDialog
  ) {}

  ngOnInit(): void {
    this.wordService.getAll().subscribe(
      data=>{
        this.words = data;
      }
    )
  }


  openReportDialog(): void {
    const dialogRef = this.dialog.open(ReportDialogComponent, {
    width: '300px', // задайте нужную ширину
    height: '70px', // задайте нужную высоту
  });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        const formData = new FormData();
        formData.append('file', result);
        console.log({'status': 'ok'});
        this.http.post(Constants.WORDS_API + '/save', formData).subscribe(response => {
          console.log(response);
        });
      }
    });
  }

}
