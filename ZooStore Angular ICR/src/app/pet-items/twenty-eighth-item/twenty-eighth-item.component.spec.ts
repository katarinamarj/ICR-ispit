import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwentyEighthItemComponent } from './twenty-eighth-item.component';

describe('TwentyEighthItemComponent', () => {
  let component: TwentyEighthItemComponent;
  let fixture: ComponentFixture<TwentyEighthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TwentyEighthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TwentyEighthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
