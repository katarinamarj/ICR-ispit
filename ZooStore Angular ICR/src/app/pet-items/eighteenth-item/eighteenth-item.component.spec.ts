import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EighteenthItemComponent } from './eighteenth-item.component';

describe('EighteenthItemComponent', () => {
  let component: EighteenthItemComponent;
  let fixture: ComponentFixture<EighteenthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EighteenthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EighteenthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
