import {Component, OnInit} from '@angular/core';
import {PathService} from "../../service/path.service";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";

@Component({
  selector: 'app-path',
  templateUrl: './path.component.html',
  styleUrl: './path.component.css'
})
export class PathComponent implements OnInit{

  public pathForm!: FormGroup;

  constructor(
    private pathService:PathService,
    private fb: FormBuilder,
    public router: Router
  ) {
  }

  ngOnInit(): void {
    this.pathForm = this.createForm()
  }


  private createForm() {
    return this.fb.group({
      path: ['', Validators.compose([Validators.required])],
    })
  }

  submit() {
    console.log(this.pathForm.value.path)
    this.pathService.setPath(this.pathForm.value.path).subscribe(data => {
      console.log(data)
      this.router.navigate(['words'])
      }
    )
  }
}
