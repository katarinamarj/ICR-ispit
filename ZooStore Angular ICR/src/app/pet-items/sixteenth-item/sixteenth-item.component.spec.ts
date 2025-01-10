import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SixteenthItemComponent } from './sixteenth-item.component';

describe('SixteenthItemComponent', () => {
  let component: SixteenthItemComponent;
  let fixture: ComponentFixture<SixteenthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SixteenthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SixteenthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
