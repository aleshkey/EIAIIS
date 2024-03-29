import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import {MaterialModule} from "./material-module";
import { PathComponent } from './components/path/path.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { WordsComponent } from './components/words/words.component';
import {HttpClient, HttpClientModule} from "@angular/common/http";
import {
  MatCell, MatCellDef,
  MatColumnDef,
  MatHeaderCell, MatHeaderCellDef,
  MatHeaderRow,
  MatHeaderRowDef,
  MatRow, MatRowDef,
  MatTable
} from "@angular/material/table";
import { WordComponent } from './components/word/word.component';
import { SearchComponent } from './components/search/search.component';
import {MatAutocomplete, MatAutocompleteTrigger, MatOption} from "@angular/material/autocomplete";
import {MatTooltip} from "@angular/material/tooltip";
import {MatSelect} from "@angular/material/select";
import {MatCheckbox} from "@angular/material/checkbox";
import { ReportDialogComponent } from './components/report-dialog/report-dialog.component';

@NgModule({
  declarations: [
    AppComponent,
    PathComponent,
    WordsComponent,
    WordComponent,
    SearchComponent,
    ReportDialogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MaterialModule,
    HttpClientModule,
    ReactiveFormsModule,
    MatCell,
    MatHeaderCell,
    MatTable,
    MatHeaderRow,
    MatRow,
    MatColumnDef,
    MatHeaderRowDef,
    MatRowDef,
    MatCellDef,
    MatHeaderCellDef,
    FormsModule,
    MatAutocomplete,
    MatOption,
    MatAutocompleteTrigger,
    MatTooltip,
    MatSelect,
    MatCheckbox
  ],
  providers: [
    provideClientHydration(),
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
