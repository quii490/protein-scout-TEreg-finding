---
type: protein-evaluation
gene: "CBWD2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CBWD2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CBWD2 |
| 蛋白名称 | Zinc-regulated GTPase metalloprotein activator 1B |
| 蛋白大小 | 395 aa / 44.0 kDa |
| UniProt ID | Q8IUF1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 395 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=2 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=75.1; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | CobW-likC_sf; CobW-like_C; CobW/HypB/UreG_nucleotide-bd |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=63 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=2 broad=2
- AF pLDDT=75.1 PDB=0
- InterPro: CobW-likC_sf; CobW-like_C; CobW/HypB/UreG_nucleotide-bd
- Pfam: cobW; CobW_C
- PPI degree=63 ChIP: None
37020999: Using multi-tissue transcriptome-wide association study to identify candidate su | 42020408: Genetic determinants of fatigue up to 2 years after radiotherapy in prostate can

### 深度机制分析

CBWD2编码锌调控GTPase金属蛋白激活因子1B（Zinc-regulated GTPase metalloprotein activator 1B），其结构域架构由CobW/HypB/UreG家族的三个保守模块组成：N端的CobW-like核苷酸结合域（IPR003495、IPR027417）负责GTP/GDP选择性结合，C端的CobW-like C结构域（IPR011629、IPR036627）介导锌配位和靶蛋白相互作用。Pfam条目PF02492（cobW）覆盖全长结构域，该家族蛋白在应激条件下通过GTPase活性和金属配位双功能方式实现功能开关。

从机制上看，CBWD2作为锌伴侣蛋白（zinc chaperone），通过psi-PxLVp基序识别METAP1的C6H2型锌指结构，形成对接复合物后由CXCC基序转移锌离子以激活甲硫氨酸氨肽酶活性。这一过程对蛋白翻译效率具有广泛调控作用，可能间接影响包括转座子编码蛋白在内的新生多肽链加工。AlphaFold pLDDT为75.1（395 aa / 44.0 kDa），结构域折叠较为完整，但缺乏实验PDB验证。

PPI网络显示CBWD2属于一个小型同源基因簇（CBWD1-6），与CBWD1（STRING评分929）、CBWD3（828）、CBWD6（828）存在强同源互作线，此外与TCERG1（748）的关联暗示其可能参与转录延伸调控。BioGRID数据进一步揭示了与PAN2（poly(A)核酸酶）、CUL3（E3泛素连接酶支架）、AGO2（RISC复合物核心成分）的潜在互作。AGO2的连接尤为值得关注——若CBWD2通过AGO2间接参与miRNA/siRNA介导的基因沉默通路，则其对TE衍生的内源性siRNA加工可能产生调控效应。

TE调控相关性方面，该蛋白缺乏核定位证据，但其锌转运功能可能通过以下间接途径影响TE：（1）锌稳态调控影响锌指转录因子（如KRAB-ZFP家族）的功能，KRAB-ZFP是已知的TE沉默核心因子；（2）METAP1的激活影响核糖体上TE衍生多肽的N端甲硫氨酸切除效率；（3）CUL3底物连接介导的泛素化降解可能涉及TE编码蛋白的周转。尽管目前证据薄弱（归一化67.8/100），CBWD2在金属蛋白激活与转录延伸交叉节点上的位置使其成为值得后续关注的候选分子。

### 4. 总体评价
**67.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Zinc-regulated GTPase metalloprotein activator 1B

**功能**: Zinc chaperone that directly transfers zinc cofactor to target metalloproteins, thereby activating them. Catalyzes zinc insertion into the active site of methionine aminopeptidase METAP1, which function to cleave the initiator methionine from polypeptides during or after protein translation. Mechanistically, the N-terminal psi-PxLVp motif binds to the C6H2-type zinc finger of inactive form of METAP1. After formation of the docked complex, zinc is transferred from the CXCC motif in the GTPase dom

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036627 |
| InterPro | IPR011629 |
| InterPro | IPR003495 |
| InterPro | IPR027417 |
| InterPro | IPR051316 |
| Pfam | PF02492 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CBWD1 | STRING | 929 |
| CBWD3 | STRING | 828 |
| CBWD6 | STRING | 828 |
| TCERG1 | STRING | 748 |
| PAN2 | BioGRID | 1 |
| CUL3 | BioGRID | 1 |
| AGO2 | BioGRID | 1 |
| HSPA12A | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8IUF1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CBWD2

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000136682

![](https://images.proteinatlas.org/42759/575_B4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42759/575_B4_2_blue_red_green.jpg)

### PubMed

**Count: 2**

| PMID | Title |
|---|---|
| 42020408 | Genetic determinants of fatigue up to 2 years after radiotherapy in prostate cancer patients. |
| 37020999 | Using multi-tissue transcriptome-wide association study to identify candidate susceptibility genes for respiratory infectious diseases. |
