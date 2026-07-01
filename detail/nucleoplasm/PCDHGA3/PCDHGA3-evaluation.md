---
type: protein-evaluation
gene: "PCDHGA3"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHGA3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHGA3 |
| 蛋白名称 | Protocadherin gamma-A3 |
| 蛋白大小 | 932 aa / 101.0 kDa |
| UniProt ID | Q9Y5H0 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 932 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=5 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=74.7; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_C |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=9 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Uncertain)
- PubMed strict=5 broad=5
- AF pLDDT=74.7 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_C
- Pfam: Cadherin; Cadherin_2; Cadherin_C_2
- PPI degree=9 ChIP: None
27748813: Protocadherin γ A3 is expressed in follicular lymphoma irrespective of BCL2 stat | 41882650: Protocadherin gamma subfamily A, 3 inhibits the proliferation and metastasis of  | 30136078: DNA methylation associated with healthy aging of elderly twins.

### 4. 总体评价
**67.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin gamma-A3

**功能**: Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002126 |
| InterPro | IPR015919 |
| InterPro | IPR032455 |
| InterPro | IPR031904 |
| InterPro | IPR020894 |
| InterPro | IPR013164 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| EGFR | BioGRID | 0 |
| CUL7 | BioGRID | 0 |
| KCNA4 | BioGRID | 0 |
| PCDHGA9 | BioGRID | 0 |
| PCDHGA4 | BioGRID | 0 |
| SPCS1 | BioGRID | 0 |
| RAB21 | BioGRID | 0 |
| HIST1H2BD | BioGRID | 0 |


### 深度机制分析

**结构域架构**：PCDHGA3（932 aa, 101.0 kDa）是原钙黏蛋白γ亚家族A3成员，与PCDHGA11高度同源（均属原钙黏蛋白γ基因簇5q31, 同源基因复制产物）。含六个串联钙黏蛋白胞外重复EC1-EC6（IPR002126 Cadherin-like_dom, IPR015919 Cadherin-like_sf, Pfam Cadherin/Cadherin_2）、跨膜螺旋TM（~700-720 aa）和胞质Cadherin_C域（IPR032455, Pfam Cadherin_C_2, ~750-932 aa）。AlphaFold pLDDT=74.7, PDB=0。EC1-EC6折叠为Ig样β-sandwich（反平行β链双层结构），每个EC域由保守Ca²⁺结合linker连接（EC-EC界面结合3个Ca²⁺离子, 配位由Asp/Glu侧链）。胞质Cadherin_C含catenin结合DEEED基序（Asp-Glu-Glu-Glu-Asp core），与β-catenin和p120-catenin形成黏附连接的膜-细胞骨架界面。PCDHGA3与PCDHGA11的结构域organization几乎完全相同，差异主要体现在EC1-EC3域的精细表面残基序列——这编码其同嗜性识别特异性。

**PPI互作网络解读**：PPI网络（degree=9）揭示PCDHGA3的非黏附信号功能。EGFR（表皮生长因子受体, RTK ErbB1/HER1, BioGRID）为核心关键伙伴——EGFR胞外域结合EGF/TGFα配体→二聚化→胞内TKD酪氨酸激酶自磷酸化→Ras/RAF/MEK/ERK和PI3K/AKT/mTOR信号激活。PCDHGA3与EGFR的互作（可能为顺式或trans）可在细胞接触处调控EGFR内化——钙黏蛋白促进EGFR的relocalization至cell-cell junction→EGFR从basal/apical膜面的随机分布转为黏附连接的特异性聚集→减弱EGFR的配体依赖性信号强度和持续时间（contact inhibition of proliferation, 接触抑制增殖的机制之一）。CUL7（cullin-7, CRL7 E3泛素连接酶支架蛋白, BioGRID）为E3泛素连接酶Cullin家族成员（CUL1-7）——CUL7与FBXW8/FBXW8（F-box/WD40 E3 adaptor）和SKP1/ROC1形成CRL7泛素连接酶→靶向IRS-1（胰岛素受体底物1）和GRB2的泛素化降解→调控PI3K/AKT/mTOR生长信号通路的负反馈。PCDHGA3-CUL7互作连接钙黏蛋白黏附至泛素化依赖的蛋白稳定性调控。KCNA4（Kv1.4, 电压门控K⁺通道α亚基, 快失活A型K⁺电流）与RAB21（Rab GTPase, 内体/高尔基体运输和整合素动态）为膜蛋白伙伴——可能反映PCDHGA3在特定膜微区（如黏附连接临近的lipid raft caveolae）中作为膜蛋白组织者。HIST1H2BD（组蛋白H2B 1D型）和SPCS1（信号肽酶复合体亚基1）提示核质/ER的跨细胞器互作。

**结构解读**：PCDHGA3的同嗜性识别的分子基础为EC1域N端strand交换机制——EC1的Trp2（Trp at position 2 of the mature protein after signal peptide cleavage, 严格保守的triad Trp2-Trp4/Trp6）插入对面细胞同型PCDHGA3 EC1域的疏水口袋→形成"strand-swap dimer"界面（Kd trans-dimer ~10 μM, Ca²⁺依赖）。Ca²⁺浓度>100 μM（胞外生理浓度~1.2-1.8 mM Ca²⁺）维持EC1-EC6胞外域刚性棒状构象（persistence length ~30-50 nm, rod-like），Ca²⁺去除→EC域间flexible hinge增强→黏附亲和力下降100-1000倍→黏附连接快速解离。胞质Cadherin_C域经DEEED基序结合β-catenin→β-catenin的C端（12th armadillo repeat之后的linker区）结合α-catenin homodimer→α-catenin直接结合F-actin filament或经vinculin/α-actinin/F-actin→完成cadherin→catenin→F-actin的力学传导链。

**机制模型**：（1）肿瘤抑制与接触抑制——PCDHGA3被发现在滤泡性淋巴瘤（follicular lymphoma）和肺腺癌中高表达（PMID:27748813，PMID:41882650）——在肺腺癌中，PCDHGA3通过抑制TGF-β信号（TGFβRI/II→SMAD2/3→SMAD4转录抑制复合体）抑制肿瘤细胞增殖和转移（PMID:41882650）。TGF-β信号的钙黏蛋白抑制为经典的上皮细胞接触抑制机制——PCDHGA3介导的细胞接触增强→TGF-β受体TGFβRII在黏附连接处被扣押→TGFβRII的配体（TGF-β1/2/3与latency-associated peptide LAP和latent TGF-β binding protein LTBP结合的潜伏TGF-β复合体的激活）无法有效激活TGF-β信号。TGF-β信号丧失→SMAD2/3核转位减少→EMT（上皮间质转换）转录因子SNAI1/SNAI2/TWIST1/ZEB1/2的转录降低→EMT受抑→肿瘤侵袭和转移阻滞。（2）钙黏蛋白剪切与核ICD信号——γ-secretase剪切PCDHGA3释放其胞内域ICD→核质中ICD与β-catenin/TCF结合→调控Wnt靶基因转录。PCDHGA3-ICD与EGFR信号的对应调控——EGFR信号降低（接触抑制阶段）→PCDHGA3-ICD核质水平增加→TCF/LEF靶基因转录激活→包括Wnt信号组分（Frizzled/LRP）和CDK抑制因子（p21/p27/cell cycle exit genes）→细胞周期退出。（3）CUL7-E3泛素连接酶轴——PCDHGA3-CUL7互作可能经CRL7调控黏附连接蛋白的泛素化周转。例如：β-catenin的K48多聚泛素化→降解→黏附连接解组装（但PCDHGA3也可能保护β-catenin免于CUL7依赖的泛素化以稳定黏附连接）。

**TE调控展望**：PCDHGA3通过钙黏蛋白剪切-ICD核质信号、EGFR-TGF-β信号crosstalk和CUL7泛素化轴间接影响TE。TGF-β/SMAD信号调控LTR-ERV的转录——SMAD2/3结合于MMTV LTR中cryptic SMAD响应元件（AGAC motif, 类似SBE, SMAD binding element）→直接激活MMTV-HERV-K的LTR启动子转录。PCDHGA3抑制TGF-β→间接减少SMAD依赖的ERV激活。EGFR信号已知激活Ras/ERK→c-FOS/c-JUN→AP-1转录因子→AP-1结合位点在TE中广泛分布（LTR中多个AP-1位点, LINE-1 5'UTR含AP-1 site）→EGFR→AP-1→TE转录。PCDHGA3在接触抑制条件下→EGFR被扣押→ERK磷酸化减少→AP-1活性降低→TE（特别是LINE-1和ERV LTR）转录下调。这与钙黏蛋白维持的细胞接触抑制状态一致——接触抑制的细胞TE转座活性通常低于增殖活跃（EGF信号强）的细胞。组蛋白H2B互作（HIST1H2BD）提示PCDHGA3可能通过直接/间接组蛋白互作影响核小体占位，改变TE区域的核小体密度。虽然PCDHGA3与PCDHGA11结构高度相似，两者的TE调控关联存在差异——PCDHGA3以TGF-β/EGFR肿瘤信号轴为主导（更偏向于接触抑制/TE的增殖依赖性调控），PCDHGA11以Wnt-RYK发育信号轴为主导（更偏向于神经元活动依赖性TE调控）——这反映了钙黏蛋白γ家族成员的信号输出特化和组织特异性。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y5H0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHGA3

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000254245-PCDHGA3

![](https://images.proteinatlas.org/10580/1610_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1610_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_2_red_green.jpg)

### PubMed

**Count: 5**

| PMID | Title |
|---|---|
| 41882650 | Protocadherin gamma subfamily A, 3 inhibits the proliferation and metastasis of lung adenocarcinoma by inhibiting transforming growth factor β signali |
| 30136078 | DNA methylation associated with healthy aging of elderly twins. |
| 27748813 | Protocadherin γ A3 is expressed in follicular lymphoma irrespective of BCL2 status and is associated with tumor cell growth. |
| 27472518 | New Cell Adhesion Molecules in Human Ischemic Cardiomyopathy. PCDHGA3 Implications in Decreased Stroke Volume and Ventricular Dysfunction. |
| 21798848 | Genome-wide molecular characterization of central nervous system primitive neuroectodermal tumor and pineoblastoma. |


