---
type: protein-evaluation
gene: "KANK2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KANK2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KANK2 |
| 蛋白名称 | KN motif and ankyrin repeat domain-containing protein 2 |
| 蛋白大小 | 851 aa / 91.2 kDa |
| UniProt ID | Q63ZY3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 851 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=34 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=60.1; PDB=3 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ankyrin_rpt; Ankyrin_rpt-contain_sf; KANK1-4 |
| PPI | 8/10 | x3 | 24.0 | PPI degree=281 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=34 broad=52
- AF pLDDT=60.1 PDB=3
- InterPro: Ankyrin_rpt; Ankyrin_rpt-contain_sf; KANK1-4
- Pfam: Ank; Ank_2; KN_motif
- PPI degree=281 ChIP: None
35271662: Identification of the shared gene signatures and pathways between sarcopenia and | 37460977: Talin2 and KANK2 functionally interact to regulate microtubule dynamics, paclita | 38253280: Transcriptional mechanism of E2F1/TFAP2C/NRF1 in regulating KANK2 gene in nephro

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: KN motif and ankyrin repeat domain-containing protein 2

**功能**: Involved in transcription regulation by sequestering in the cytoplasm nuclear receptor coactivators such as NCOA1, NCOA2 and NCOA3 (PubMed:17476305). Involved in regulation of caspase-independent apoptosis by sequestering the proapoptotic factor AIFM1 in mitochondria (PubMed:22371500). Pro-apoptotic stimuli can induce its proteasomal degradation allowing the translocation of AIFM1 to the nucleus to induce apoptosis (PubMed:22371500). Involved in the negative control of vitamin D receptor signali

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002110 |
| InterPro | IPR036770 |
| InterPro | IPR047184 |
| InterPro | IPR021939 |
| Pfam | PF00023 |
| Pfam | PF12796 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NCOA1 | BioGRID | 1 |
| NCOA3 | BioGRID | 1 |
| NCOA2 | BioGRID | 1 |
| CSNK2A1 | BioGRID | 1 |
| DCP1A | BioGRID | 1 |
| DCP1B | BioGRID | 1 |
| EIF4E | BioGRID | 1 |
| LMO1 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q63ZY3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000197256-KANK2

![](https://images.proteinatlas.org/15643/2043_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/15643/2043_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/15643/165_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/15643/165_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/15643/126_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/15643/126_E11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 52**

| 42252217 | [Uterine inflammatory myofibroblastic tumor: a clinicopathological and molecular genetic analysis of eight cases]. | Zhonghua Bing Li Xue Za Zhi 2026 |
| 42032724 | Regulation of reticular adhesions by KANK2 and talin2 in two melanoma cell lines. | Cell Commun Signal 2026 |
| 42002769 | Integrated m6A methylome and transcriptome profiling of mRNAs and lncRNAs in nasal mucosal epithelial cells of allergic  | Clin Epigenetics 2026 |

### 深度机制分析

KANK2是一种多功能支架蛋白（851 aa, 91.2 kDa），其结构域架构由N端的KN基序（KN_motif）和C端的多个Ankyrin重复序列（Ank/Ank_2, IPR002110）组成，中间区域含有KANK1-4保守结构域（IPR047184）。Ankyrin重复是已知的蛋白-蛋白相互作用模块，呈螺旋-转角-螺旋折叠，在KANK2中以串联重复形式形成延展的溶剂可及表面，能够同时招募多个结合伙伴。AlphaFold预测整体pLDDT仅60.1，提示该蛋白含有大量内在无序区域（IDR），这些IDR可能通过液-液相分离（LLPS）形成生物分子凝聚体，从而在胞质和核质之间动态分配。

KANK2的功能核心在于其双重定位的转录调控机制（PMID:17476305）。在胞质中，KANK2通过KN基序和Ankyrin重复捕获核受体共激活因子NCOA1（SRC-1）、NCOA2（GRIP1）和NCOA3（AIB1），将其扣押在胞质中从而阻止它们入核激活靶基因转录。这一"胞质扣押"（cytoplasmic sequestration）机制为KANK2提供了间接但高效的转录负调控能力。PPI网络（BioGRID degree=281）证实了与NCOA1/2/3的高置信度互作（评分=1）。

KANK2还参与调控caspase非依赖的凋亡程序（PMID:22371500）。它通过在线粒体中扣押促凋亡因子AIFM1来抑制凋亡；在促凋亡刺激下，KANK2经蛋白酶体降解后释放AIFM1，后者转位至核内诱导染色质凝集和DNA断裂。这揭示了KANK2作为"凋亡闸门"的分子开关角色。与CSNK2A1（酪蛋白激酶2）和EIF4E（翻译起始因子）的互作暗示其也在翻译调控层面发挥作用。

鉴于KANK2通过扣押转录共激活因子来间接抑制核内转录活动，其对TE调控的潜在影响在于：若KANK2降解或被竞争性结合伙伴释放，NCOA1/2/3即可入核激活核受体靶基因及可能的下游TE位点。维生素D受体信号通路的负调控功能进一步扩展了其转录调控网络。未来研究应关注：是否有TE来源的启动子或增强子受KANK2-NCOA轴调控；KANK2在特定应激条件下是否发生液-液相分离以调节其扣押活性；PMID:38253280提示的E2F1/TFAP2C/NRF1转录调控KANK2的机制是否在TE去抑制中发挥作用。pLDDT=60.1的低置信区域可能正是介导LLPS和多功能接头的关键无序区。

