import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {PathComponent} from "./components/path/path.component";
import {WordsComponent} from "./components/words/words.component";
import {WordComponent} from "./components/word/word.component";

const routes: Routes = [
  {path: 'path', component: PathComponent},
  {path: 'words', component: WordsComponent},
  {path: 'words/:id', component: WordComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
