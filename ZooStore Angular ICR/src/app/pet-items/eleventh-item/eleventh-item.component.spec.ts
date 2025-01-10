import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EleventhItemComponent } from './eleventh-item.component';

describe('EleventhItemComponent', () => {
  let component: EleventhItemComponent;
  let fixture: ComponentFixture<EleventhItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EleventhItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EleventhItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
