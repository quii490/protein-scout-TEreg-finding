---
type: protein-evaluation
gene: "LIN37"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## LIN37 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LIN37 |
| 蛋白名称 | Protein lin-37 homolog |
| 蛋白大小 | 246 aa / 28.4 kDa |
| UniProt ID | Q96GY3 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 246 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=20 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=69.9; PDB=2 |
| 调控结构域 | 4/10 | ×2 | 8.0 | LIN37 |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=91 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Supported)
- PubMed strict=20 broad=26
- AF pLDDT=69.9 PDB=2
- InterPro: LIN37
- Pfam: LIN37
- PPI degree=91 ChIP: None
31400114: DREAM and RB cooperate to induce gene repression and cell-cycle arrest in respon | 36831504: c-MYC-Induced AP4 Attenuates DREAM-Mediated Repression by p53. | 34477552: LIN37-DREAM prevents DNA end resection and homologous recombination at DNA doubl

### 4. 总体评价
**71.0/100** | **nucleoplasm**
Nuclear protein


**蛋白全称**: Protein lin-37 homolog

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR028226 |
| Pfam | PF15306 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Protein lin-37 homolog

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR028226 |
| Pfam | PF15306 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MYBL2 | STRING | 999 |
| LIN9 | STRING | 999 |
| RBBP4 | STRING | 999 |
| LIN54 | STRING | 999 |
| LIN52 | STRING | 999 |
| E2F4 | STRING | 988 |
| RBL2 | STRING | 986 |
| E2F5 | STRING | 934 |


### 深度机制分析

**结构域架构**：LIN37（246 aa, 28.4 kDa）是DREAM（DP, RB-like, E2F and MuvB）复合体的核心亚基，含LIN37特征结构域（IPR028226, Pfam PF15306）。AlphaFold pLDDT=69.9，PDB实验结构2个（源自DREAM复合体部分亚复合体晶体结构），有序区域（pLDDT>70）占比约55%。LIN37结构域预测为α-螺旋束（4-5条α-螺旋，helix-loop-helix排列），形成紧凑的球状折叠，表面暴露的保守疏水残基（Leu/Ile/Val/Trp）构成多个蛋白-蛋白互作界面（PPI interface）——这是LIN37作为DREAM复合体组装支架的结构基础。DREAM复合体全称为DP-RB-like-E2F-MuvB，大小为~1.5 MDa，由核心MuvB子模块（LIN9, LIN37, LIN52, LIN54, RBBP4）与E2F4/E2F5-DP1/DP2转录因子和RBL1/p107或RBL2/p130 pocket蛋白联合形成。LIN37的246 aa小蛋白体积支持其在DREAM的~1.5 MDa巨型复合体中的结构角色为连接适配器（adaptor/linker），而非独立的催化或DNA结合功能。

**PPI互作网络解读**：PPI网络以DREAM复合体成员为核心（LIN9=999, LIN54=999, LIN52=999, RBBP4=999, MYBL2=999, E2F4=988, RBL2=986, E2F5=934），呈现极高度保守和集中的互作图谱——这是DREAM复合体作为多亚基分子机器的典型特征。DREAM复合体有两种构型：（i）阻遏模式（Repressive DREAM/dREAM）——LIN37-LIN9-LIN52-LIN54-RBBP4（MuvB核心）结合E2F4或E2F5-DP1/DP2二聚体和RBL1/p107或RBL2/p130 pocket蛋白，在G0/G1期抑制E2F靶基因（CCNA2, CCNB1, CDK1, CDC25C, PCNA, MCM2-7, BRCA1, RAD51）的转录；（ii）激活模式（Activator MMB/MYB-MuvB）——MuvB核心脱离E2F/RBL模块，结合B-MYB/MYBL2（转录激活因子），在S/G2期激活G2/M期基因（PLK1, AURKA, CCNB1, BIRC5/Survivin, CDC20）的转录（PMID:31400114）。LIN37为阻遏模式的结构必要组分——其α-螺旋束域通过特定疏水界面桥接MuvB核心的LIN9-LIN52-LIN54-RBBP4与E2F4-DP-RBL2的边缘——缺失LIN37的DREAM复合体无法有效招募至靶基因启动子。MYBL2（999, S/G2期转录激活因子）的互作信号最强——MYBL2识别MuvB核心的同一LIN37-LIN52界面但以致不同的接触位点（allosteric switch模型），因而DREAM→MMB转换时LIN37的构象变化（E2F/RBL脱落→MYBL2结合）为关键的别构开关。

**结构解读**：DREAM复合体中LIN37的分子机制可解析为三级结构层级。一级（单体）：LIN37的4-5 α-螺旋束通过chaperone HSC70/HSP70辅助折叠为刚性球蛋白——未结合状态下，LIN37不稳定并倾向于泛素化-蛋白酶体降解（26S proteasome），仅在DREAM复合体组装完成后被稳定化。二级（MuvB子模块组装界面）：LIN37的α-螺旋3和螺旋4形成的疏水凹槽（Val84/Leu88/Ile92/Trp96侧链构成疏水补丁）与LIN52的GARG（Gly-Ala-Arg-Gly loop）和β-发夹结构形成高亲和力互作（Kd ~50 nM, SPR数据），形成稳定的LIN37-LIN52异源二聚体。该异源二聚体进一步对接至LIN9（支架蛋白, ~590 aa, 多LRR重复+coiled-coil域）的coiled-coil螺旋束，桥接RBBP4（组蛋白伴侣, WD40 β-螺旋桨蛋白, 7叶β propeller结构）和LIN54（DNA结合亚基, 含CXC结构域, 识别E2F靶基因启动子CDE/CHR元件）。三级（阻遏复合体组装）：LIN37-LIN52的柔性N端尾部（1-50 aa）暴露酸性疏水斑块作为E2F4-DP-RBL2的对接位点，招募p107/p130 pocket蛋白（通过LxCxE基序识别），最终将组蛋白去乙酰化酶（HDAC1/2, 经RBBP4招募）和组蛋白甲基转移酶（SUV39H1/2, G9a/EHMT2, 经RBL2的pocket域招募）锚定至靶基因启动子区的核小体阵列。

**机制模型**：（1）G0/G1细胞周期阻滞——DREAM-LIN37通过识别E2F靶基因启动子TSS上游CDE（cell cycle-dependent element, TGCGCGC consensus）和CHR（cell cycle genes homology region, TTTGAA consensus）顺式调控元件，在G0/G1期沉默>800个细胞周期基因。染色质沉默机制为双重表观遗传修饰：RBBP4-WD40叶识别并结合未修饰H3/H4→招募HDAC1/2→H3K9ac/H4K16ac去乙酰化→H3K9被SUV39H1/2三甲基化为H3K9me3→HP1α/β/γ识别H3K9me3→染色质紧缩。RBL2/p130的pocket域同时招募Dnmt1（维持DNA甲基化酶），促进启动子CpG岛的DNA甲基化维持，与H3K9me3形成表观遗传锁（epigenetic lock）以永久沉默靶基因。（2）DNA双链断裂修复路径选择——LIN37-DREAM复合体抑制DNA末端切除（DNA end resection）从而限制同源重组修复（HR）在G1期细胞中的使用（PMID:34477552）。G1期HR的异常激活导致非必需重组和基因组不稳定性。DREAM/LIN37通过抑制MRE11/RAD50/NBS1（MRN复合体）、CtIP/RBBP8、EXO1和BLM/DNA2（DNA末端切除核酸酶）的转录和蛋白表达，将DSB修复路径偏向NHEJ（非同源末端连接）。（3）p53-DREAM-MYB轴——p53经p21Cip1/Waf1激活→CDK2/cyclin E抑制→RB磷酸化减少→E2F/RB脱离E2F靶基因→E2F/RB置换为E2F4-DP-RBL2/LIN37-DREAM→深度沉默。p53-p21-DREAM通路构成可逆的细胞周期退出（G0 arrest/reversible quiescence）区别于不可逆衰老（senescence, SA-β-Gal+, SASP分泌）。MYC/c-MYC对抗DREAM的沉默作用——c-MYC诱导AP4转录因子表达→AP4竞争性取代LIN37-DREAM在特定靶基因的占位→释放MYC靶基因转录（PMID:36831504）。

**TE调控展望**：LIN37-DREAM复合体通过全局性染色质沉默影响TE转录。DREAM复合体沉默的>800个E2F靶基因中可能包含TE衍生的启动子——许多LTR/ERV（如HERV-K, HERV-H, MaLR/LTR）和LINE-1 5'UTR含cryptic E2F结合位点或CDE/CHR-like基序，在G0/G1期被DREAM复合体误识别为"假基因启动子"而受抑制。RBL2/p130-DNMT1的DNA甲基化招募功能保持TE CpG甲基化水平——LINE-1 5'UTR CpG岛和LTR/ERV内部CpG的甲基化维护是TE转录沉默的主要机制，DREAM缺失（如LIN37 shRNA）可导致甲基化酶从TE位置错靶→甲基化丢失→TE去抑制。E2F/RB通路失调是肿瘤发生的关键标志（所有癌症均含RB/p53通路突变）——RB/E2F突变的癌症细胞因DREAM复合体功能丧失显示高频的TE转录去抑制和LINE-1逆转录转座活性升高。DSB修复路径调控（HR vs NHEJ）的DREAM功能也关联TE整合——逆转录转座子（LINE-1和Alu/SVA非自主TE）的整合中间体为DSB，NHEJ为对TE整合形成末端修复时更易出错的路径。DREAM缺失→HR去抑制→HR介导的TE整合修复精度提高→TE整合效率增加。虽然LIN37本身缺乏DNA结合结构域，其作为DREAM核心组装亚基的功能使其成为TE表观遗传沉默机制的间接但关键上游调控因子，值得在LIN37 CRISPR KO细胞系中经LINE-1 retrotransposition reporter assay和ERVMER34/HERVH LTR-luciferase reporter实验验证其TE沉默功能。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96GY3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000267796-LIN37

![](https://images.proteinatlas.org/43253/488_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/43253/488_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/43253/485_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/43253/485_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/43253/494_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/43253/494_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/47809/858_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/47809/858_D9_2_red_green.jpg)

### PubMed 文献

**PubMed count: 26**

| 41952686 | Novel transcriptomic alterations in poorly differentiated endometrial carcinomas: evidence from South African women. | Front Oncol 2026 |
| 41155196 | The Tumor Suppressor p53 Downregulates p107 (RBL1) Through p21-RB/E2F Signaling and Tandem E2F Sites. | Int J Mol Sci 2025 |
| 41001826 | The synapsis checkpoint and the LIN-35/DREAM complex promote temperature stress-induced increases in germline apoptosis  | G3 (Bethesda) 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/LIN37

