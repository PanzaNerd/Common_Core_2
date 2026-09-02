# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/31 17:06:11 by matthias          #+#    #+#              #
#    Updated: 2026/08/31 17:07:25 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(temp_str: str) -> int:
      temperature = int(temp_str)
      if temperature > 40:
              raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
      if temperature < 0:
              raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
      return temperature

def test_temperature() -> None:
      print("=== Garden Temperature Checker ===")

      print("Input data is '25'")
      temperature = input_temperature("25")
      print(f"Temperature is now {temperature}°C")

      print("Input data is 'abc'")
      try:
              input_temperature("abc")
      except Exception as e:
              print(f"Caught input_temperature error: {e}")

      print("Input data is '100'")
      try:
              input_temperature("100")
      except Exception as e:
              print(f"Caught input_temperature error: {e}")

      print("Input data is '-50'")
      try:
              input_temperature("-50")
      except Exception as e:
              print(f"Caught input_temperature error: {e}")

      print("All tests completed - program didn't crash!")


if __name__ == "__main__":
      test_temperature()
