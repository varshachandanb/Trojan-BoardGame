"""greedy best first search """
import copy
import sys

choice=[1,2,3]
#inpt=open(sys.argv[-1])
with open("input.txt","r") as inpt:
    lines=inpt.readlines()
    depth=0
    m_depth=0
    board=[]
    state={}
    scores =[]
    scores_O=0
    scores_X=0
    current_X=[]
    current_O=[]
    raid_pos=[]
    check=[]
    X_sneak_score=0
    O_sneak_score=0
    sneak_score=0
    X_sneak_pos=""
    max_util_value=0
    X_value=0
    O_value=0
    final_scores=[[0 for x in range(5)] for x in range(5)]
    free_spot=[]
    total_score=0
    max_val=-9999
    min_val=9999
    move_X=''
    move_O=''
    find_next_X={}
    find_next_O={}



class Game(object):
    def __init__(self):
        self.board=board
        self.choice=lines[0]
        self.m_depth=int(lines[2])
        self.player=lines[1]
        self.X_value=X_value
        self.O_value=O_value
        self.depth=0
        self.mx_value='-Infinity'
        self.mn_value='Infinity'
        self.value=0
        self.node="root"
        self.trial_board=[]
        self.alpha='-Infinity'
        self.beta='Infinity'

    def get_current(self,board):
        global scores_O
        global scores_X
        global current_X
        global current_O
        global free_spot
        free_spot=[]
        current_O=[]
        current_X=[]
        scores_X=0
        scores_O=0
        for m in range(0,5):
            for n in range(0,5):
                if ("X" in board[m][n]):
                    scores_X+=int(scores[m][n])
                    current_X.append(str(m)+","+str(n))
                elif ("O" in board[m][n]):
                    scores_O+=int(scores[m][n])
                    current_O.append((str(m)+","+str(n)))
                else:
                    free_spot.append((str(m)+","+str(n)))

    def get_up(self,m,n):
        return str(m+1)+","+str(n)

    def get_down(self,m,n):
        return str(m-1)+","+str(n)

    def get_right(self,m,n):
        return str(m)+","+str(n+1)

    def get_left(self,m,n):
        return str(m)+","+str(n-1)

    def Terminal_Test(self,board):
        flag=1
        for m in range(0,5):
            for n in range(0,5):
                if(board[m][n]=="*"):
                    flag=0
        return flag

    def Utility(self,board):
        gm.get_current(board)
        if("X" in player):
            return (scores_X-scores_O)
        else:
            return (scores_O-scores_X)


    def get_greedy_max_X(self,parent,depth,trial_board):
        global move_X
        global board
        parent.player='X'
        global state
        temp=[]
        m_val=0
        temp=copy.deepcopy(board)
        global find_next_X
        if(parent.Terminal_Test(parent.board)):
            return parent.Utility(parent.board)
        else:
                child=Game()
                for i in range(0,5):
                    for j in range(0,5):
                        if(trial_board[i][j]=='*'):
                            child.trial_board=copy.deepcopy(temp)
                            child.player='X'
                            child.trial_board[i][j]='X'
                            child.node=str(i)+','+str(j)
                            m_val=child.get_neighbor(child,depth,child.trial_board)
                            find_next_X[child.node]=str(m_val)
                            parent.value=max(parent.value,m_val)

                return parent.value


    def get_greedy_max_O(self,parent,depth,trial_board):
        global move_O
        global board
        parent.player='O'
        global state
        temp=[]
        m_val=0
        temp=copy.deepcopy(board)
        global find_next_O
        if(parent.Terminal_Test(parent.board)):
            # works fine
            return parent.Utility(parent.board)
        else:
                child=Game()
                for i in range(0,5):
                    for j in range(0,5):
                        if(trial_board[i][j]=='*'):
                            child.trial_board=copy.deepcopy(temp)
                            child.player='O'
                            child.trial_board[i][j]='O'
                            child.node=str(i)+','+str(j)
                            m_val=child.get_neighbor(child,depth,child.trial_board)
                            find_next_O[child.node]=str(m_val)
                            parent.value=max(parent.value,m_val)
                return parent.value

    def get_neighbor(self,parent,depth,trial_board):
            global max_util_value
            global scores_O
            global scores_X
            max_util_value=0
            util_value=0
            curr=parent.node
            tmp=parent.node.split(',')
            parent.get_current(parent.trial_board)
            m=int(tmp[0])
            n=int(tmp[1])
            if("X" in player):
                if("X" in parent.player):
                    X_present=0
                    O_present=0
                    up=gm.get_up(m,n)
                    down=gm.get_down(m,n)
                    right=gm.get_right(m,n)
                    left=gm.get_left(m,n)
                    p=up.split(',')
                    d=down.split(',')
                    r=right.split(',')
                    l=left.split(',')
                    up_score=0
                    down_score=0
                    right_score=0
                    left_score=0
                    curr_score=int(scores[m][n])
                    #check up
                    if(int(p[0])!=-1 and int(p[1])!=5 and int(p[0])!=5 and int(p[1])!=-1):
                        ngh_up=trial_board[int(p[0])][int(p[1])]
                        if(ngh_up=='O'):
                            O_present+=1
                            up_score=int(scores[int(p[0])][int(p[1])])
                        elif(ngh_up=='X'):
                            X_present=1
                    #check down
                    if(int(d[0])!=-1 and int(d[1])!=5 and int(d[0])!=5 and int(d[1])!=-1):
                        ngh_down=trial_board[int(d[0])][int(d[1])]
                        if(ngh_down=='O'):
                            O_present+=1
                            down_score=int(scores[int(d[0])][int(d[1])])
                        elif(ngh_down=='X'):
                            X_present=1
                    #check right
                    if(int(r[0])!=-1 and int(r[1])!=5 and int(r[0])!=5 and int(r[1])!=-1):
                        ngh_rgh=trial_board[int(r[0])][int(r[1])]
                        if(ngh_rgh=='O') :
                            O_present+=1
                            right_score=int(scores[int(r[0])][int(r[1])])
                        elif(ngh_rgh=='X'):
                            X_present=1
                    #check left
                    if(int(l[0])!=-1 and int(l[1])!=5 and int(l[0])!=5 and int(l[1])!=-1):
                        ngh_lft=trial_board[int(l[0])][int(l[1])]
                        if(ngh_lft=='O'):
                            O_present+=1
                            left_score=int(scores[int(l[0])][int(l[1])])
                        elif(ngh_lft=='X'):
                            X_present=1
                    #check if sneak
                    if(X_present==0) or (O_present==0) :
                        max_util_value=(scores_X)-scores_O
                        parent.trial_board[m][n]='X'
                     #else its a raid
                    else:
                        parent.X_value=left_score+up_score+right_score+down_score
                        if(up_score>0):
                            parent.trial_board[int(p[0])][int(p[1])]='X'
                            scores_O-=up_score
                        if(down_score>0):
                            scores_O-=down_score
                            parent.trial_board[int(d[0])][int(d[1])]='X'
                        if(right_score>0):
                            scores_O-=right_score
                            parent.trial_board[int(r[0])][int(r[1])]='X'
                        if(left_score>0):
                            scores_O-=left_score
                            parent.trial_board[int(l[0])][int(l[1])]='X'
                        max_util_value=(parent.X_value+scores_X)-scores_O
                elif("O" in parent.player):
                    X_present=0
                    O_present=0
                    up=gm.get_up(m,n)
                    down=gm.get_down(m,n)
                    right=gm.get_right(m,n)
                    left=gm.get_left(m,n)
                    p=up.split(',')
                    d=down.split(',')
                    r=right.split(',')
                    l=left.split(',')
                    up_score=0
                    down_score=0
                    right_score=0
                    left_score=0
                    curr_score=int(scores[m][n])
                    #check up
                    if(int(p[0])!=-1 and int(p[1])!=5 and int(p[0])!=5 and int(p[1])!=-1):
                        ngh_up=trial_board[int(p[0])][int(p[1])]
                        if(ngh_up=='X'):
                            X_present+=1
                            up_score=int(scores[int(p[0])][int(p[1])])
                            #scores_O-=up_score
                        elif(ngh_up=='O'):
                            O_present=1
                    #check down
                    if(int(d[0])!=-1 and int(d[1])!=5 and int(d[0])!=5 and int(d[1])!=-1):
                        ngh_down=trial_board[int(d[0])][int(d[1])]
                        if(ngh_down=='X'):
                            X_present+=1
                            down_score=int(scores[int(d[0])][int(d[1])])
                        elif(ngh_down=='O'):
                            O_present=1
                    #check right
                    if(int(r[0])!=-1 and int(r[1])!=5 and int(r[0])!=5 and int(r[1])!=-1):
                        ngh_rgh=trial_board[int(r[0])][int(r[1])]
                        if(ngh_rgh=='X') :
                            X_present+=1
                            right_score=int(scores[int(r[0])][int(r[1])])
                        elif(ngh_rgh=='O'):
                            O_present=1
                    #check left
                    if(int(l[0])!=-1 and int(l[1])!=5 and int(l[0])!=5 and int(l[1])!=-1):
                        ngh_lft=trial_board[int(l[0])][int(l[1])]
                        if(ngh_lft=='X'):
                            X_present+=1
                            left_score=int(scores[int(l[0])][int(l[1])])
                        elif(ngh_lft=='O'):
                            O_present=1
                    #check if sneak
                    if(X_present==0) or (O_present==0) :
                        max_util_value=scores_X-scores_O
                        parent.trial_board[m][n]='O'
                     #else its a raid
                    else:
                        parent.O_value=left_score+up_score+right_score+down_score
                        if(up_score>0):
                            parent.trial_board[int(p[0])][int(p[1])]='O'
                            scores_X-=up_score
                        if(down_score>0):
                            scores_X-=down_score
                            parent.trial_board[int(d[0])][int(d[1])]='O'
                        if(right_score>0):
                            scores_X-=right_score
                            parent.trial_board[int(r[0])][int(r[1])]='O'
                        if(left_score>0):
                            scores_X-=left_score
                            parent.trial_board[int(l[0])][int(l[1])]='O'
                        max_util_value=(scores_X)-(scores_O+parent.O_value)
                return max_util_value
            elif("O" in player):
                if("X" in parent.player):
                    X_present=0
                    O_present=0
                    up=gm.get_up(m,n)
                    down=gm.get_down(m,n)
                    right=gm.get_right(m,n)
                    left=gm.get_left(m,n)
                    p=up.split(',')
                    d=down.split(',')
                    r=right.split(',')
                    l=left.split(',')
                    up_score=0
                    down_score=0
                    right_score=0
                    left_score=0
                    curr_score=int(scores[m][n])
                    #check up
                    if(int(p[0])!=-1 and int(p[1])!=5 and int(p[0])!=5 and int(p[1])!=-1):
                        ngh_up=trial_board[int(p[0])][int(p[1])]
                        if(ngh_up=='O'):
                            O_present+=1
                            up_score=int(scores[int(p[0])][int(p[1])])
                            #scores_O-=up_score
                        elif(ngh_up=='X'):
                            X_present=1
                    #check down
                    if(int(d[0])!=-1 and int(d[1])!=5 and int(d[0])!=5 and int(d[1])!=-1):
                        ngh_down=trial_board[int(d[0])][int(d[1])]
                        if(ngh_down=='O'):
                            O_present+=1
                            down_score=int(scores[int(d[0])][int(d[1])])
                        elif(ngh_down=='X'):
                            X_present=1
                    #check right
                    if(int(r[0])!=-1 and int(r[1])!=5 and int(r[0])!=5 and int(r[1])!=-1):
                        ngh_rgh=trial_board[int(r[0])][int(r[1])]
                        if(ngh_rgh=='O') :
                            O_present+=1
                            right_score=int(scores[int(r[0])][int(r[1])])
                        elif(ngh_rgh=='X'):
                            X_present=1
                    #check left
                    if(int(l[0])!=-1 and int(l[1])!=5 and int(l[0])!=5 and int(l[1])!=-1):
                        ngh_lft=trial_board[int(l[0])][int(l[1])]
                        if(ngh_lft=='O'):
                            O_present+=1
                            left_score=int(scores[int(l[0])][int(l[1])])
                        elif(ngh_lft=='X'):
                            X_present=1
                    #check if sneak
                    if(X_present==0) or (O_present==0) :
                        max_util_value=scores_O-(scores_X)
                        parent.trial_board[m][n]='X'
                        conquer_O=[]
                     #else its a raid
                    else:
                        parent.X_value=left_score+up_score+right_score+down_score
                        if(up_score>0):
                            parent.trial_board[int(p[0])][int(p[1])]='X'
                            scores_O-=up_score
                        if(down_score>0):
                            scores_O-=down_score
                            parent.trial_board[int(d[0])][int(d[1])]='X'
                        if(right_score>0):
                            scores_O-=right_score
                            parent.trial_board[int(r[0])][int(r[1])]='X'
                        if(left_score>0):
                            scores_O-=left_score
                            parent.trial_board[int(l[0])][int(l[1])]='X'
                        max_util_value=(scores_O)-(parent.X_value+scores_X)

                elif('O' in parent.player):
                    X_present=0
                    O_present=0
                    up=gm.get_up(m,n)
                    down=gm.get_down(m,n)
                    right=gm.get_right(m,n)
                    left=gm.get_left(m,n)
                    p=up.split(',')
                    d=down.split(',')
                    r=right.split(',')
                    l=left.split(',')
                    up_score=0
                    down_score=0
                    right_score=0
                    left_score=0
                    curr_score=int(scores[m][n])
                    #check up
                    if(int(p[0])!=-1 and int(p[1])!=5 and int(p[0])!=5 and int(p[1])!=-1):
                        ngh_up=trial_board[int(p[0])][int(p[1])]
                        if(ngh_up=='X'):
                            X_present+=1
                            up_score=int(scores[int(p[0])][int(p[1])])
                            #scores_O-=up_score
                        elif(ngh_up=='O'):
                            O_present=1
                    #check down
                    if(int(d[0])!=-1 and int(d[1])!=5 and int(d[0])!=5 and int(d[1])!=-1):
                        ngh_down=trial_board[int(d[0])][int(d[1])]
                        if(ngh_down=='X'):
                            X_present+=1
                            down_score=int(scores[int(d[0])][int(d[1])])
                        elif(ngh_down=='O'):
                            O_present=1
                    #check right
                    if(int(r[0])!=-1 and int(r[1])!=5 and int(r[0])!=5 and int(r[1])!=-1):
                        ngh_rgh=trial_board[int(r[0])][int(r[1])]
                        if(ngh_rgh=='X') :
                            X_present+=1
                            right_score=int(scores[int(r[0])][int(r[1])])
                        elif(ngh_rgh=='O'):
                            O_present=1
                    #check left
                    if(int(l[0])!=-1 and int(l[1])!=5 and int(l[0])!=5 and int(l[1])!=-1):
                        ngh_lft=trial_board[int(l[0])][int(l[1])]
                        if(ngh_lft=='X'):
                            X_present+=1
                            left_score=int(scores[int(l[0])][int(l[1])])
                        elif(ngh_lft=='O'):
                            O_present=1
                    #check if sneak
                    if(X_present==0) or (O_present==0) :
                        max_util_value=scores_O-scores_X
                        parent.trial_board[m][n]='O'
                     #else its a raid
                    else:
                        parent.O_value=left_score+up_score+right_score+down_score
                        if(up_score>0):
                            parent.trial_board[int(p[0])][int(p[1])]='O'
                            scores_X-=up_score
                        if(down_score>0):
                            scores_X-=down_score
                            parent.trial_board[int(d[0])][int(d[1])]='O'
                        if(right_score>0):
                            scores_X-=right_score
                            parent.trial_board[int(r[0])][int(r[1])]='O'
                        if(left_score>0):
                            scores_X-=left_score
                            parent.trial_board[int(l[0])][int(l[1])]='O'
                        max_util_value=(scores_O+parent.O_value)-scores_X
                return max_util_value

    def get_max_X(self,parent,log,depth,trial_board):
        global move_X
        parent.player='O'
        global state
        temp_board=[]
        min_val=-9999
        if(parent.Terminal_Test(parent.board)):
            with open("next_state.txt","w") as opt:
                for i in range(0,5):
                    for j in range(0,5):
                        opt.write(parent.board[i][j])
                    opt.write('\n')
            opt.close()
            return parent.Utility(parent.board)
        else:
            child=Game()
            if(depth==parent.m_depth):
                parent.player='O'
                parent.mn_value=parent.get_neighbor(parent,depth,parent.trial_board)
                #parent.mn_value=parent.result_X(parent,depth,parent.trial_board)
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+'\n')
                move_O=parent.mn_value
                return parent.mn_value
            else:
                global max_val
                max_val=-9999
                for i in range(0,5):
                    for j in range(0,5):
                        if(trial_board[i][j]=='*'):
                            child.trial_board=copy.deepcopy(parent.trial_board)
                            child.player='X'
                            child.trial_board[i][j]='X'
                            child.node=str(i)+','+str(j)
                            log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+'\n')
                            if('-Infinity' in str(parent.mx_value)):
                                    parent.mx_value=-9999
                            if((depth+1)==m_depth):
                                parent.mx_value=max(parent.mx_value,child.get_min_O(child,log,depth+1,parent.trial_board))
                            else:
                                child.get_neighbor(child,depth,child.trial_board)
                                child.mn_value='Infinity'
                                parent.mx_value=max(parent.mx_value,child.get_min_O(child,log,depth+1,child.trial_board))
                            trial_board=copy.deepcopy(parent.trial_board)
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+'\n')
                return parent.mx_value

    def get_min_O(self,parent,log,depth,trial_board):
        parent.player='X'
        global state
        global find_next_X
        if(parent.Terminal_Test(parent.board)):
            with open("next_state.txt","w") as opt:
                for i in range(0,5):
                    for j in range(0,5):
                        opt.write(parent.board[i][j])
                    opt.write('\n')
            opt.close()
            return parent.Utility(parent.board)
        else:
            child=Game()
            if(depth==parent.m_depth):
                parent.player='X'
                parent.mx_value=parent.get_neighbor(parent,depth,parent.trial_board)
                #parent.result_X(parent,depth,parent.trial_board)
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+'\n')
                if(parent.m_depth==1):
                    find_next_X[parent.node]=str(parent.mx_value)
                return parent.mx_value
            else:
                global min_val
                min_val=9999
                for i in range(0,5):
                    for j in range(0,5):
                        if(trial_board[i][j]=='*'):
                            child.trial_board=copy.deepcopy(parent.trial_board)
                            child.player='O'
                            child.trial_board[i][j]='O'
                            child.node=str(i)+','+str(j)
                            #parent.mn_value='Infinity'
                            log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+'\n')
                            if('Infinity' in str(parent.mn_value)):
                                parent.mn_value=9999
                            if((depth+1)==m_depth):
                                parent.mn_value=min(parent.mn_value,child.get_max_X(child,log,depth+1,parent.trial_board))
                            else:
                                child.get_neighbor(child,depth,child.trial_board)
                                child.mx_value='-Infinity'
                                parent.mn_value=min(parent.mn_value,child.get_max_X(child,log,depth+1,child.trial_board))
                            trial_board=copy.deepcopy(parent.trial_board)
                if(depth==1):
                    find_next_X[parent.node]=str(parent.mn_value)
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+'\n')
                return parent.mn_value

    def get_max_O(self,parent,log,depth,trial_board):
        parent.player='X'
        global state
        min_val=-9999
        if(parent.Terminal_Test(parent.board)):
            with open("next_state.txt","w") as opt:
                for i in range(0,5):
                    for j in range(0,5):
                        opt.write(parent.board[i][j])
                    opt.write('\n')
            opt.close()
            return parent.Utility(parent.board)
        else:
            parent.get_current(parent.board)
            child=Game()
            if(depth==parent.m_depth):
                parent.player='X'
                parent.mn_value=parent.get_neighbor(parent,depth,parent.trial_board)
                #parent.mn_value=parent.result_O(parent,depth,parent.trial_board)
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+'\n')

                return parent.mn_value
            else:
                global max_val
                max_val=-9999
                for i in range(0,5):
                    for j in range(0,5):
                        if(trial_board[i][j]=='*'):
                            child.trial_board=copy.deepcopy(parent.trial_board)
                            child.player='O'
                            child.trial_board[i][j]='O'
                            child.node=str(i)+','+str(j)
                            #parent.mx_value='-Infinity'
                            log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+'\n')
                            if('-Infinity' in str(parent.mx_value)):
                                    parent.mx_value=-9999
                            if((depth+1)==m_depth):
                                parent.mx_value=max(parent.mx_value,child.get_min_X(child,log,depth+1,parent.trial_board))
                            else:
                                child.get_neighbor(child,depth,child.trial_board)
                                child.mn_value='Infinity'
                                parent.mx_value=max(parent.mx_value,child.get_min_X(child,log,depth+1,child.trial_board))
                            trial_board=copy.deepcopy(parent.trial_board)
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+'\n')
                return parent.mx_value

    def get_min_X(self,parent,log,depth,trial_board):
        parent.player='O'
        global state
        global find_next_O
        if(parent.Terminal_Test(parent.board)):
            with open("next_state.txt","w") as opt:
                for i in range(0,5):
                    for j in range(0,5):
                        opt.write(parent.board[i][j])
                    opt.write('\n')
            opt.close()
            return parent.Utility(parent.board)
        else:
            child=Game()

            if(depth==parent.m_depth):
                parent.player='O'
                parent.mx_value=parent.get_neighbor(parent,depth,parent.trial_board)
                #parent.mx_value=parent.result_O(parent,depth,parent.trial_board)
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+'\n')
                if(parent.m_depth==1):
                    find_next_O[parent.node]=str(parent.mx_value)
                return parent.mx_value
            else:
                global min_val
                min_val=9999
                for i in range(0,5):
                    for j in range(0,5):
                        if(trial_board[i][j]=='*'):
                            child.trial_board=copy.deepcopy(parent.trial_board)
                            child.player='X'
                            child.trial_board[i][j]='X'
                            child.node=str(i)+','+str(j)
                            #parent.mn_value='Infinity'
                            log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+'\n')
                            if('Infinity' in str(parent.mn_value)):
                                parent.mn_value=9999
                            if((depth+1)==m_depth):
                                parent.mn_value=min(parent.mn_value,child.get_max_O(child,log,depth+1,parent.trial_board))
                            else:
                                child.get_neighbor(child,depth,child.trial_board)
                                child.mx_value='-Infinity'
                                parent.mn_value=min(parent.mn_value,child.get_max_O(child,log,depth+1,child.trial_board))
                            trial_board=copy.deepcopy(parent.trial_board)
                if(depth==1):
                    find_next_O[parent.node]=str(parent.mn_value)
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+'\n')
                return parent.mn_value

    def minimax_next_move_X(self,gm,find_next_X,move_X):
        same_state=[]
        min_vl=0
        gm.player='X'
        for key in find_next_X:
            if(find_next_X[key] in move_X):
                same_state.append(key)
        if not same_state:
            with open("next_state.txt","w") as opt:
                for i in range(0,5):
                    for j in range(0,5):
                        opt.write(gm.board[i][j])
                    opt.write('\n')
                opt.close()
        else:
            min_vl=min(same_state)
            k=min_vl.split(',')
            gm.trial_board[int(k[0])][int(k[1])]='X'
            gm.node=min_vl
            gm.get_neighbor(gm,depth,gm.trial_board)
            with open("next_state.txt","w") as opt:
                for i in range(0,5):
                    for j in range(0,5):
                        opt.write(gm.board[i][j])
                    opt.write('\n')
            opt.close()

    def minimax_next_move_O(self,gm,find_next_O,move_O):
        same_state=[]
        min_vl=0
        global preference
        gm.player='O'
        for key in find_next_O:
            if(find_next_O[key] in move_O):
                same_state.append(key)
        if not same_state:
            with open("next_state.txt","w") as opt:
                for i in range(0,5):
                    for j in range(0,5):
                        opt.write(gm.board[i][j])
                    opt.write('\n')
                opt.close()
        else:
            min_vl=min(same_state)
            k=min_vl.split(',')
            gm.trial_board[int(k[0])][int(k[1])]='O'
            gm.node=min_vl
            gm.get_neighbor(gm,depth,gm.trial_board)
            with open("next_state.txt","w") as opt:
                for i in range(0,5):
                    for j in range(0,5):
                        opt.write(gm.board[i][j])
                    opt.write('\n')
            opt.close()

    def get_ab_max_X(self,parent,log,depth,trial_board):
        global move_X
        parent.player='O'
        global state
        temp_board=[]
        min_val=-9999
        if(parent.Terminal_Test(parent.board)):
            with open("next_state.txt","w") as opt:
                for i in range(0,5):
                    for j in range(0,5):
                        opt.write(parent.board[i][j])
                    opt.write('\n')
            opt.close()
            return parent.Utility(parent.board)

        else:
            child=Game()
            if(depth==parent.m_depth):
                parent.player='O'
                parent.beta=self.beta
                parent.alpha=self.alpha
                parent.mn_value=parent.get_neighbor(parent,depth,parent.trial_board)
                if('9999' in str(parent.mn_value)):
                    parent.mn_value='Infinity'
                if('-9999' in str(parent.alpha)):
                    parent.alpha='-Infinity'
                if('9999' in str(parent.beta)):
                    parent.beta='Infinity'
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                move_O=parent.mn_value
                return parent.mn_value
            else:
                global max_val
                max_val=-9999
                for i in range(0,5):
                    for j in range(0,5):
                        if(trial_board[i][j]=='*'):
                            child.trial_board=copy.deepcopy(parent.trial_board)
                            child.player='X'
                            child.trial_board[i][j]='X'
                            child.alpha=parent.alpha
                            child.beta=parent.beta
                            child.node=str(i)+','+str(j)
                            if('9999' in str(parent.mn_value)):
                                parent.mn_value='Infinity'
                            if('-9999' in str(parent.alpha)):
                                parent.alpha='-Infinity'
                            if('9999' in str(parent.beta)):
                                parent.beta='Infinity'
                            log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')

                            if('-Infinity' in str(parent.mx_value)):
                                parent.mx_value=-9999
                            if('-Infinity' in (str(parent.alpha))):
                                parent.alpha=-9999
                            if('Infinity' in (str(parent.beta))):
                                parent.beta=9999
                            if((depth+1)==m_depth):
                                parent.mx_value=max(parent.mx_value,parent.get_ab_min_O(child,log,depth+1,parent.trial_board))
                                if(parent.mx_value>=parent.beta):
                                    if('9999' in str(parent.mn_value)):
                                        parent.mn_value='Infinity'
                                    if('-9999' in str(parent.alpha)):
                                        parent.alpha='-Infinity'
                                    if('9999' in str(parent.beta)):
                                        parent.beta='Infinity'
                                    log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                                    return parent.mx_value
                                else:
                                    parent.alpha=max(parent.alpha,parent.mx_value)
                            else:
                                child.get_neighbor(child,depth,child.trial_board)
                                child.mn_value='Infinity'
                                parent.mx_value=max(parent.mx_value,parent.get_ab_min_O(child,log,depth+1,child.trial_board))
                                if(parent.mx_value>=parent.beta):
                                    if('9999' in str(parent.mn_value)):
                                        parent.mn_value='Infinity'
                                    if('-9999' in str(parent.alpha)):
                                        parent.alpha='-Infinity'
                                    if('9999' in str(parent.beta)):
                                        parent.beta='Infinity'
                                    log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                                    return parent.mx_value
                                else:
                                    parent.alpha=max(parent.alpha,parent.mx_value)
                            trial_board=copy.deepcopy(parent.trial_board)
                if('9999' in str(parent.mn_value)):
                    parent.mn_value='Infinity'
                if('-9999' in str(parent.alpha)):
                    parent.alpha='-Infinity'
                if('9999' in str(parent.beta)):
                    parent.beta='Infinity'
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                move_X=parent.mx_value
                return parent.mx_value

    def get_ab_min_O(self,parent,log,depth,trial_board):
        parent.player='X'
        global state
        global find_next_X
        if(parent.Terminal_Test(parent.board)):
            with open("next_state.txt","w") as opt:
                for i in range(0,5):
                    for j in range(0,5):
                        opt.write(parent.board[i][j])
                    opt.write('\n')
            opt.close()
            return parent.Utility(parent.board)
        else:
            child=Game()
            if(depth==parent.m_depth):
                parent.player='X'
                parent.mx_value=parent.get_neighbor(parent,depth,parent.trial_board)
                parent.beta=self.beta
                parent.alpha=self.alpha
                if('9999' in str(parent.mn_value)):
                    parent.mn_value='Infinity'
                if('-9999' in str(parent.alpha)):
                    parent.alpha='-Infinity'
                if('9999' in str(parent.beta)):
                    parent.beta='Infinity'
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                move_X=parent.mx_value
                return parent.mx_value
            else:
                global min_val
                min_val=9999
                for i in range(0,5):
                    for j in range(0,5):
                        if(trial_board[i][j]=='*'):
                            child.trial_board=copy.deepcopy(parent.trial_board)
                            child.player='O'
                            child.trial_board[i][j]='O'
                            child.node=str(i)+','+str(j)
                            child.alpha=parent.alpha
                            child.beta=parent.beta
                            #parent.mn_value='Infinity'
                            if('9999' in str(parent.mn_value)):
                                parent.mn_value='Infinity'
                            if('-9999' in str(parent.alpha)):
                                parent.alpha='-Infinity'
                            if('9999' in str(parent.beta)):
                                parent.beta='Infinity'
                            log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')

                            if('Infinity' in str(parent.mn_value)):
                                parent.mn_value=9999
                            if('-Infinity' in (str(parent.alpha))):
                                parent.alpha=-9999
                            if('Infinity' in (str(parent.beta))):
                                parent.beta=9999
                            if((depth+1)==m_depth):
                                parent.mn_value=min(parent.mn_value,parent.get_ab_max_X(child,log,depth+1,parent.trial_board))
                                if(parent.mn_value<=parent.alpha):
                                    if('9999' in str(parent.mn_value)):
                                        parent.mn_value='Infinity'
                                    if('-9999' in str(parent.alpha)):
                                        parent.alpha='-Infinity'
                                    if('9999' in str(parent.beta)):
                                        parent.beta='Infinity'
                                    log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                                    return parent.mn_value
                                else:
                                    parent.beta=min(parent.beta,parent.mn_value)
                            else:
                                child.get_neighbor(child,depth,child.trial_board)
                                child.mx_value='-Infinity'
                                parent.mn_value=min(parent.mn_value,parent.get_ab_max_X(child,log,depth+1,child.trial_board))
                                if(parent.mn_value<=parent.alpha):
                                    if('9999' in str(parent.mn_value)):
                                        parent.mn_value='Infinity'
                                    if('-9999' in str(parent.alpha)):
                                        parent.alpha='-Infinity'
                                    if('9999' in str(parent.beta)):
                                        parent.beta='Infinity'
                                    log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                                    return parent.mn_value
                                else:
                                    parent.beta=min(parent.beta,parent.mn_value)
                            trial_board=copy.deepcopy(parent.trial_board)
                if(depth==1):
                    find_next_X[parent.node]=str(parent.mn_value)
                if('9999' in str(parent.mn_value)):
                    parent.mn_value='Infinity'
                if('-9999' in str(parent.alpha)):
                    parent.alpha='-Infinity'
                if('9999' in str(parent.beta)):
                    parent.beta='Infinity'
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                return parent.mn_value

    def get_ab_max_O(self,parent,log,depth,trial_board):
        global move_O
        parent.player='X'
        global state
        temp_board=[]
        min_val=-9999
        if(parent.Terminal_Test(parent.board)):
            with open("next_state.txt","w") as opt:
                for i in range(0,5):
                    for j in range(0,5):
                        opt.write(parent.board[i][j])
                    opt.write('\n')
            opt.close()
            return parent.Utility(parent.board)
        else:
            #parent.get_current(parent.board)
            child=Game()
            if(depth==parent.m_depth):
                parent.player='X'
                parent.beta=self.beta
                parent.alpha=self.alpha
                parent.mn_value=parent.get_neighbor(parent,depth,parent.trial_board)
                if('9999' in str(parent.mn_value)):
                    parent.mn_value='Infinity'
                if('-9999' in str(parent.alpha)):
                    parent.alpha='-Infinity'
                if('9999' in str(parent.beta)):
                    parent.beta='Infinity'
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                move_X=parent.mn_value
                return parent.mn_value
            else:
                global max_val
                max_val=-9999
                for i in range(0,5):
                    for j in range(0,5):
                        if(trial_board[i][j]=='*'):
                            child.trial_board=copy.deepcopy(parent.trial_board)
                            child.player='O'
                            child.trial_board[i][j]='O'
                            child.alpha=parent.alpha
                            child.beta=parent.beta
                            child.node=str(i)+','+str(j)
                            if('9999' in str(parent.mn_value)):
                                parent.mn_value='Infinity'
                            if('-9999' in str(parent.alpha)):
                                parent.alpha='-Infinity'
                            if('9999' in str(parent.beta)):
                                parent.beta='Infinity'
                            log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')

                            if('-Infinity' in str(parent.mx_value)):
                                parent.mx_value=-9999
                            if('-Infinity' in (str(parent.alpha))):
                                parent.alpha=-9999
                            if('Infinity' in (str(parent.beta))):
                                parent.beta=9999
                            if((depth+1)==m_depth):
                                parent.mx_value=max(parent.mx_value,parent.get_ab_min_X(child,log,depth+1,parent.trial_board))
                                if(parent.mx_value>=parent.beta):
                                    if('9999' in str(parent.mn_value)):
                                        parent.mn_value='Infinity'
                                    if('-9999' in str(parent.alpha)):
                                        parent.alpha='-Infinity'
                                    if('9999' in str(parent.beta)):
                                        parent.beta='Infinity'
                                    log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                                    return parent.mx_value
                                else:
                                    parent.alpha=max(parent.alpha,parent.mx_value)
                            else:
                                child.get_neighbor(child,depth,child.trial_board)
                                child.mn_value='Infinity'
                                parent.mx_value=max(parent.mx_value,parent.get_ab_min_X(child,log,depth+1,child.trial_board))
                                if(parent.mx_value>=parent.beta):
                                    if('9999' in str(parent.mn_value)):
                                        parent.mn_value='Infinity'
                                    if('-9999' in str(parent.alpha)):
                                        parent.alpha='-Infinity'
                                    if('9999' in str(parent.beta)):
                                        parent.beta='Infinity'
                                    log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                                    return parent.mx_value
                                else:
                                    parent.alpha=max(parent.alpha,parent.mx_value)
                            trial_board=copy.deepcopy(parent.trial_board)
                if('9999' in str(parent.mn_value)):
                    parent.mn_value='Infinity'
                if('-9999' in str(parent.alpha)):
                    parent.alpha='-Infinity'
                if('9999' in str(parent.beta)):
                    parent.beta='Infinity'
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                move_O=parent.mx_value
                return parent.mx_value

    def get_ab_min_X(self,parent,log,depth,trial_board):
        parent.player='O'
        global state
        global find_next_O
        if(parent.Terminal_Test(parent.board)):
            with open("next_state.txt","w") as opt:
                for i in range(0,5):
                    for j in range(0,5):
                        opt.write(parent.board[i][j])
                    opt.write('\n')
            opt.close()
            return parent.Utility(parent.board)
        else:
            child=Game()
            if(depth==parent.m_depth):
                parent.player='O'
                parent.mx_value=parent.get_neighbor(parent,depth,parent.trial_board)
                parent.beta=self.beta
                parent.alpha=self.alpha
                if('9999' in str(parent.mn_value)):
                    parent.mn_value='Infinity'
                if('-9999' in str(parent.alpha)):
                    parent.alpha='-Infinity'
                if('9999' in str(parent.beta)):
                    parent.beta='Infinity'
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mx_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                move_O=parent.mx_value
                return parent.mx_value
            else:
                global min_val
                min_val=9999
                for i in range(0,5):
                    for j in range(0,5):
                        if(trial_board[i][j]=='*'):
                            child.trial_board=copy.deepcopy(parent.trial_board)
                            child.player='X'
                            child.trial_board[i][j]='X'
                            child.node=str(i)+','+str(j)
                            child.alpha=parent.alpha
                            child.beta=parent.beta
                            #parent.mn_value='Infinity'
                            if('9999' in str(parent.mn_value)):
                                parent.mn_value='Infinity'
                            if('-9999' in str(parent.alpha)):
                                parent.alpha='-Infinity'
                            if('9999' in str(parent.beta)):
                                parent.beta='Infinity'
                            log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')

                            if('Infinity' in str(parent.mn_value)):
                                parent.mn_value=9999
                            if('-Infinity' in (str(parent.alpha))):
                                parent.alpha=-9999
                            if('Infinity' in (str(parent.beta))):
                                parent.beta=9999
                            if((depth+1)==m_depth):
                                parent.mn_value=min(parent.mn_value,parent.get_ab_max_O(child,log,depth+1,parent.trial_board))
                                if(parent.mn_value<=parent.alpha):
                                    if('9999' in str(parent.mn_value)):
                                        parent.mn_value='Infinity'
                                    if('-9999' in str(parent.alpha)):
                                        parent.alpha='-Infinity'
                                    if('9999' in str(parent.beta)):
                                        parent.beta='Infinity'
                                    log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                                    return parent.mn_value
                                else:
                                    parent.beta=min(parent.beta,parent.mn_value)
                            else:
                                child.get_neighbor(child,depth,child.trial_board)
                                child.mx_value='-Infinity'
                                parent.mn_value=min(parent.mn_value,parent.get_ab_max_O(child,log,depth+1,child.trial_board))
                                if(parent.mn_value<=parent.alpha):
                                    if('9999' in str(parent.mn_value)):
                                        parent.mn_value='Infinity'
                                    if('-9999' in str(parent.alpha)):
                                        parent.alpha='-Infinity'
                                    if('9999' in str(parent.beta)):
                                        parent.beta='Infinity'
                                    log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                                    return parent.mn_value
                                else:
                                    parent.beta=min(parent.beta,parent.mn_value)
                            trial_board=copy.deepcopy(parent.trial_board)
                if(depth==1):
                    find_next_O[parent.node]=str(parent.mn_value)
                if('9999' in str(parent.mn_value)):
                    parent.mn_value='Infinity'
                if('-9999' in str(parent.alpha)):
                    parent.alpha='-Infinity'
                if('9999' in str(parent.beta)):
                    parent.beta='Infinity'
                log.write(state[parent.node]+','+str(depth)+','+str(parent.mn_value)+','+str(parent.alpha)+','+str(parent.beta)+'\n')
                return parent.mn_value




if __name__ == '__main__':
    gm=Game()
    choice=gm.choice
    player=gm.player
    m_depth=gm.m_depth
    sc1=lines[3].rstrip('\r\n').split(' ')
    sc2=lines[4].rstrip('\r\n').split(' ')
    sc3=lines[5].rstrip('\r\n').split(' ')
    sc4=lines[6].rstrip('\r\n').split(' ')
    sc5=lines[7].rstrip('\r\n').split(' ')
    scores=[sc1,sc2,sc3,sc4,sc5]
    board0 = list(lines[8].rstrip('\n'))
    board1 = list(lines[9].rstrip('\n'))
    board2 = list(lines[10].rstrip('\n'))
    board3 = list(lines[11].rstrip('\n'))
    board4 = list(lines[12].rstrip('\n'))
    board = [board0,board1,board2,board3,board4]
    gm.trial_board=copy.deepcopy(board)
    gm.board=copy.deepcopy(board)
    gm.get_current(board)
    util_val=0
    state={'root':'root','0,0':'A1','0,1':'B1','0,2':'C1','0,3':'D1','0,4':'E1','1,0':'A2','1,1':'B2','1,2':'C2','1,3':'D2','1,4':'E2','2,0':'A3','2,1':'B3','2,2':'C3','2,3':'D3','2,4':'E3','3,0':'A4','3,1':'B4','3,2':'C4','3,3':'D4','3,4':'E4','4,0':'A5','4,1':'B5','4,2':'C5','4,3':'D5','4,4':'E5'}
    #preference={'0,0':'1','0,1':'2','0,2':'3','0,3':'4','0,4':'5','1,0':'6','1,1':'7','1,2':'8','1,3':'9','1,4':'10','2,0':'11','2,1':'12','2,2':'13','2,3':'14','2,4':'15','3,0':'16','3,1':'17','3,2':'18','3,3':'19','3,4':'20','4,0':'21','4,1':'22','4,2':'23','4,3':'24','4,4':'25'}
    inpt.close()
    if("1" in choice):
        parent=Game()
        if("X" in player):
            parent.trial_board=board
            parent.mx_value=parent.get_greedy_max_X(parent,depth,parent.trial_board)
            parent.minimax_next_move_X(parent,find_next_X,str(parent.mx_value))
        elif("O" in player):
            parent.trial_board=board
            parent.mx_value=parent.get_greedy_max_O(parent,depth,parent.trial_board)
            parent.minimax_next_move_O(parent,find_next_O,str(parent.mx_value))


    elif("2" in choice):
        with open("traverse_log.txt","w") as log:
            log.write("Node"+','+"Depth"+','+"Value"+'\n')
            parent=Game()
            parent.trial_board=board
            if("X" in player):
                parent.mx_value=parent.get_max_X(parent,log,depth,parent.trial_board)
                parent.minimax_next_move_X(parent,find_next_X,str(parent.mx_value))
            elif("O" in player):
                parent.mx_value=parent.get_max_O(parent,log,depth,parent.trial_board)
                parent.minimax_next_move_O(parent,find_next_O,str(parent.mx_value))

    elif("3" in choice):
        with open("traverse_log.txt","w") as log:
            log.write("Node"+','+"Depth"+','+"Value"+','+"Alpha"+','+"Beta"+'\n')
            parent=Game()
            parent.trial_board=board
            if("X" in player):
                parent.mx_value=parent.get_ab_max_X(parent,log,depth,parent.trial_board)
                parent.minimax_next_move_X(parent,find_next_X,str(parent.mx_value))
            elif("O" in player):
                parent.mx_value=parent.get_ab_max_O(parent,log,depth,parent.trial_board)
                parent.minimax_next_move_O(parent,find_next_O,str(parent.mx_value))

















