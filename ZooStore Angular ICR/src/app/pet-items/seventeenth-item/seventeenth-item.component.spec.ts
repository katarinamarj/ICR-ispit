import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SeventeenthItemComponent } from './seventeenth-item.component';

describe('SeventeenthItemComponent', () => {
  let component: SeventeenthItemComponent;
  let fixture: ComponentFixture<SeventeenthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SeventeenthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SeventeenthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
