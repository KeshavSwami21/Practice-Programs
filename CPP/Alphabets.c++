#include <iostream>
#include <string.h>
using namespace std;

class Alphabets
{

public:
    string str;
    int row, col;

    void Input()
    {
        cout << "Enter the Alphabet you want to print on output screen: ";
        cin.ignore();
        getline(cin, str);
    }

    void Logic()
    {
        for (auto x : str)
        {
            char word = x;
            switch (tolower(word))
            {
            case 'a':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if (((col == 0 or col == 3) and (row > 0)) or ((row == 0 or row == 3) and (col == 1 or col == 2)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'b':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 0) or ((col == 3) and (row != 0 and row != 3 and row != 6)) or ((row == 0 or row == 3 or row == 6) and (col == 1 or col == 2)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'c':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if (((col == 0) and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'd':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 0) or ((col == 3) and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col < 3)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'e':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 0) or ((row == 0 or row == 6) and (col < 4)) or ((row == 3) and (col < 3)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'f':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 0) or ((row == 0) and (col < 4)) or ((row == 3) and (col < 3)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'g':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if (((col == 0) and (row != 0 and row != 6)) or ((col == 3) and (row != 0 and row != 6 and row != 2)) or ((row == 0 or row == 6) and (col == 1 or col == 2)) or ((row == 3) and (col == 2)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'h':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 0 or col == 3) or ((row == 3) and (col < 3)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'i':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 2) or ((row == 0 or row == 6) and (col < 5)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'j':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 3) or ((row == 0) and (col < 7)) or ((row == 5 or row == 4) and (col == 0)) or ((row == 6) and (col == 1 or col == 2)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'k':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 0) or ((row == 3) and (col == 1)) or ((row == 2 or row == 4) and (col == 2)) or ((row == 1 or row == 5) and (col == 3)) or ((row == 0 or row == 6) and (col == 4)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'l':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 0) or ((row == 6) and (col < 4)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'm':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 0 or col == 6) or ((row == 1) and (col == 1 or col == 5)) or ((row == 2) and (col == 2 or col == 4)) or ((row == 3) and (col == 3)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'n':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 0 or col == 6) or ((row == 1) and (col == 1)) or ((row == 2) and (col == 2)) or ((row == 3) and (col == 3)) or ((row == 4) and (col == 4)) or ((row == 5) and (col == 5)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'o':
                for (row = 0; row < 6; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if (((col == 0 or col == 4) and (row != 0 and row != 5)) or ((row == 0 or row == 5) and (col == 1 or col == 2 or col == 3)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'p':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 0) or ((col == 3) and (row == 1 or row == 2)) or ((row == 0 or row == 3) and (col < 3)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'q':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if (((col == 0 or col == 4) and (row != 0 and row != 5 and row != 6)) or ((row == 0 or row == 5) and (col == 1 or col == 2 or col == 3)) or ((row == 4) and (col == 3)) or ((row == 6) and (col == 5)) or ((row == 3) and (col == 2)) or ((row == 5) and (col == 4)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'r':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 0) or ((col == 3) and (row == 1 or row == 2)) or ((row == 0 or row == 3) and (col < 3)) or ((row == 4) and (col == 2)) or ((row == 5) and (col == 3)) or ((row == 6) and (col == 4)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 's':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if (((col == 0) and (row == 1 or row == 2 or row == 6)) or ((col == 3) and (row == 4 or row == 5)) or ((row == 3 or row == 6) and (col == 1 or col == 2)) or ((row == 0) and (col == 1 or col == 2 or col == 3)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 't':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 3) or (row == 0))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'u':
                for (row = 0; row < 6; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if (((col == 0 or col == 4) and (row != 5)) or ((row == 5) and (col == 1 or col == 2 or col == 3)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'v':
                for (row = 0; row < 4; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if (((row == 0) and (col == 0 or col == 6)) or ((row == 1) and (col == 1 or col == 5)) or ((row == 2) and (col == 2 or col == 4)) or ((row == 3) and (col == 3)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'w':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((col == 0 or col == 6) or ((row == 5) and (col == 1 or col == 5)) or ((row == 4) and (col == 2 or col == 4)) or ((row == 3) and (col == 3)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'x':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if (((col == 0 or col == 6) and (row == 0 or row == 6)) or ((col == 1 or col == 5) and (row == 1 or row == 5)) or ((col == 2 or col == 4) and (row == 2 or row == 4)) or ((row == 3) and (col == 3)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'y':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if (((row == 0) and (col == 0 or col == 6)) or ((row == 1) and (col == 1 or col == 5)) or ((row == 2) and (col == 2 or col == 4)) or ((row == 3) and (col == 3)) or ((col == 3) and (row == 4 or row == 5 or row == 6)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            case 'z':
                for (row = 0; row < 7; row++)
                {
                    for (col = 0; col < 7; col++)
                    {
                        if ((row == 0 or row == 6) or ((col == 5) and (row == 1)) or ((col == 4) and (row == 2)) or ((col == 3) and (row == 3)) or ((col == 2) and (row == 4)) or ((col == 1) and (row == 5)))
                        {
                            cout << "* ";
                        }
                        else
                        {
                            cout << "  ";
                        }
                    }
                    cout << endl;
                }
                break;

            default:
                cout << "\nPlease enter the correct alphatbet.";
                break;
            }

           word = "";
        }
    }
};

int main()
{
    Alphabets al;

    al.Input();
    al.Logic();

    return 0;
}