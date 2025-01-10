import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwentyFourthItemComponent } from './twenty-fourth-item.component';

describe('TwentyFourthItemComponent', () => {
  let component: TwentyFourthItemComponent;
  let fixture: ComponentFixture<TwentyFourthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TwentyFourthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TwentyFourthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
