import {Component, OnInit} from '@angular/core';
import {PathService} from "../../service/path.service";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";
import {FileLinker} from "@angular/compiler-cli/linker";
import { Location } from '@angular/common';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'path',
  templateUrl: './path.component.html',
  styleUrl: './path.component.css'
})
export class PathComponent implements OnInit{
  public pathForm!: FormGroup;


  constructor(
    private pathService:PathService,
    private fb: FormBuilder,
    public router: Router,
    private http: HttpClient
  ) {
  }




  ngOnInit(): void {
    this.pathForm = this.createForm()
  }

  onFileSelected(input: any): void {
    if (input.files && input.files.length > 0)
    {
      const file_to_upload = input.files[0]
      this.uploadFile(file_to_upload)
    }
  }


  uploadFile(file: File): void{
    const formData = new FormData()
    formData.append('file', file)
    console.log('data')
    this.pathService.sendRequest(formData).subscribe(data=> {
        console.log(data)
        window.location.reload()
      }
    )
  }

  private createForm() {
    return this.fb.group({
      path: ['', Validators.compose([Validators.required])],
    })
  }
}
