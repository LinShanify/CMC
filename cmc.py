import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def show_cmc(my_method_name,title,rank_no,cmc_dict):
    color = ['g','b','c','m','y','orange','brown']
    marker = ['o','s','v','X','*','.','P']
    fig, ax = plt.subplots()
    fig.suptitle(title)
    x = list(range(0, rank_no+1, 5))
    plt.ylim(0, 1.0)
    plt.xlim(1, rank_no)
    plt.xlabel('Rank')
    plt.ylabel('Matching Rates (%)')
    plt.xticks(x)
    plt.grid(True)

    method_name = []
    i = 0
    for name in cmc_dict.keys():
        if rank_no < len(cmc_dict[name]):
            temp_cmc = cmc_dict[name][:rank_no]
            r = list(range(1, rank_no+1))
        else:
            temp_cmc = cmc_dict[name]
            r = list(range(1, len(temp_cmc)+1))
        if name == my_method_name:
            globals()[name] = mlines.Line2D(r, temp_cmc, color='r', marker='*', label='{:.1f}% '.format(cmc_dict[name][0]*100)+name)
        else:
            globals()[name] = mlines.Line2D(r, temp_cmc, color=color[i], marker=marker[i], label='{:.1f}% '.format(cmc_dict[name][0]*100)+name)
            i = i+1
        ax.add_line(globals()[name])
        method_name.append(globals()[name])

    plt.legend(handles=method_name)
    plt.show()
    
def save_cmc(my_method_name,title,rank_no,cmc_dict, save_dir, dpi=500, file_type='eps'):
    color = ['g','b','c','m','y','orange','brown']
    marker = ['o','s','v','X','*','.','P']
    fig, ax = plt.subplots()
    fig.suptitle(title)
    x = list(range(0, rank_no+1, 5))
    plt.ylim(0, 1.0)
    plt.xlim(1, rank_no)
    plt.xlabel('Rank')
    plt.ylabel('Matching Rates (%)')
    plt.xticks(x)
    plt.grid(True)

    method_name = []
    i = 0
    for name in cmc_dict.keys():
        if rank_no < len(cmc_dict[name]):
            temp_cmc = cmc_dict[name][:rank_no]
            r = list(range(1, rank_no+1))
        else:
            temp_cmc = cmc_dict[name]
            r = list(range(1, len(temp_cmc)+1))
        if name == my_method_name:
            globals()[name] = mlines.Line2D(r, temp_cmc, color='r', marker='*', label='{:.1f}% '.format(cmc_dict[name][0]*100)+name)
        else:
            globals()[name] = mlines.Line2D(r, temp_cmc, color=color[i], marker=marker[i], label='{:.1f}% '.format(cmc_dict[name][0]*100)+name)
            i = i+1
        ax.add_line(globals()[name])
        method_name.append(globals()[name])

    plt.legend(handles=method_name)
    fig.savefig(save_dir+'/'+title, dpi=dpi, format=file_type)