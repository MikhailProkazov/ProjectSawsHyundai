from pydantic import BaseModel


class Saws_Parameters(BaseModel):

    saw_model: str
    saw_price: int
    saw_power: str



saw_1 = Saws_Parameters(saw_model='x 232323', saw_price= 11500, saw_power= '2.4 л.с')

print(type(saw_1.saw_price))