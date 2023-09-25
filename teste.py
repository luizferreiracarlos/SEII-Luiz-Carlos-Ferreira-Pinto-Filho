{
  "metadata": {
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    },
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "import time",
      "metadata": {
        "trusted": true
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "start = time.perf_counter()",
      "metadata": {
        "trusted": true
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "def do_something():\n    print('Sleeping 1 second...')\n    time.sleep(1)\n    print('Done sleeping...')\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "do_something()",
      "metadata": {
        "trusted": true
      },
      "execution_count": 9,
      "outputs": [
        {
          "name": "stdout",
          "text": "Sleeping 1 second...\nDone sleeping...\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "do_something()",
      "metadata": {
        "trusted": true
      },
      "execution_count": 10,
      "outputs": [
        {
          "name": "stdout",
          "text": "Sleeping 1 second...\nDone sleeping...\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "finish = time.perf_counter()",
      "metadata": {
        "trusted": true
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "print(f'Finished in {round(finish-start, 2)} second(s)')",
      "metadata": {
        "trusted": true
      },
      "execution_count": 8,
      "outputs": [
        {
          "name": "stdout",
          "text": "Finished in 210.1 second(s)\n",
          "output_type": "stream"
        }
      ]
    }
  ]
}