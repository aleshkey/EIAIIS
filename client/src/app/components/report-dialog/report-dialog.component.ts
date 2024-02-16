import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';

@Component({
  templateUrl: 'report-dialog.component.html'
})
export class ReportDialogComponent {
  selectedFile: File | null = null;

  constructor(public dialogRef: MatDialogRef<ReportDialogComponent>) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  closeDialog() {
    this.dialogRef.close(this.selectedFile);
  }
}
