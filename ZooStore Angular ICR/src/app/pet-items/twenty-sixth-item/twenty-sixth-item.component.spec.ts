import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwentySixthItemComponent } from './twenty-sixth-item.component';

describe('TwentySixthItemComponent', () => {
  let component: TwentySixthItemComponent;
  let fixture: ComponentFixture<TwentySixthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TwentySixthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TwentySixthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
