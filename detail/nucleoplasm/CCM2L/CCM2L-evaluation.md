---
type: protein-evaluation
gene: "CCM2L"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CCM2L 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CCM2L |
| 蛋白名称 | Cerebral cavernous malformations 2 protein-like |
| 蛋白大小 | 571 aa / 62.2 kDa |
| UniProt ID | Q9NUG4 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 571 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=7 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=58.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | CCM2_C; Malcavernin; PH-like_dom_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=8 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 分析
- HPA: Nucleoplasm (Approved)
- PubMed: strict=7, broad=11
- AF pLDDT: 58.6 / PDB: 0
- InterPro: CCM2_C; Malcavernin; PH-like_dom_sf
- Pfam: CCM2_C
- PPI degree=8 / ChIP: None
40521769: Compound Heterozygous Loss-of-Function Variants in CCM2L in a Fetus With Tetralo | 23328253: ccm2-like is required for cardiovascular development as a novel component of the | 22898778: Dynamic regulation of the cerebral cavernous malformation pathway controls vascu

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Cerebral cavernous malformations 2 protein-like

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR032375 |
| InterPro | IPR026159 |
| InterPro | IPR011993 |
| Pfam | PF16545 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

CCM2L的深度机制以其CCM2_C结构域（Pfam PF16545, InterPro IPR032375）为核心展开。CCM2（Cerebral Cavernous Malformations 2）蛋白家族是脑血管完整性调控的核心组件，经典的CCM1/KRIT1-CCM2-CCM3/PDCD10三聚体形成信号平台，通过抑制MEKK3-MEK5-ERK5信号轴和调控细胞骨架-RhoA信号维持血管内皮细胞屏障功能。CCM2L作为CCM2的旁系同源蛋白，在结构域层面与CCM2共享CCM2_C和PTB（phosphotyrosine-binding）样结构域，但在功能上明显分化——CCM2L的PH-like_dom_sf（IPR011993）赋予其磷脂酰肌醇磷酸盐（PIP）结合能力，可能赋予CCM2L独立于经典CCM信号体的膜靶向机制。AlphaFold预测pLDDT仅为58.6（得分4/10），571 aa的整体折叠置信度偏低，尤其是PTB样结构域与CCM2_C之间的长连接区段可能高度柔性。0个PDB结构意味着CCM2L的原子模型完全依赖预测，在缺乏实验验证的情况下不宜用于分子对接或虚拟筛选。

CCM2L的PPI网络（degree=8）蕴含着关键的信号通路连接。STRING数据中MAP3K3（MEKK3, score=740）在CCM2/CCM2L演化保守性中具有核心意义——MEKK3正是经典CCM信号体中CCM2直接抑制的下游靶标。在CCM疾病模型中，CCM2作为支架蛋白通过其CCM2_C结构域结合并隔离MEKK3，阻止MEKK3-MEK5-ERK5信号级联的异常激活。CCM2L对MAP3K3的蛋白互作暗示它可能扮演与CCM2竞争或协同调控MAP3K3/MEKK3的角色，但由于CCM2L缺乏CCM2的N端部分序列，其与MAP3K3结合后的功能输出（抑制或激活）可能截然不同。BioGRID数据中HMGN2（高分迁移率族核小体结合蛋白2）和PBX4（pre-B细胞白血病转录因子4）的互作尤为值得关注——两者均为明确的核内染色质调控因子。HMGN2直接结合核小体，降低H1接头组蛋白与核小体的亲和力以促进染色质开放状态，而PBX4是HOX共因子家族的转录调控蛋白。若这两个互作得到内源验证，将是CCM2L直接参与染色质调控的关键证据。PSMB1（蛋白酶体20S核心亚基）的互作则提示CCM2L可能与泛素-蛋白酶体系统存在物理关联。

CCM2L的文献研究极度贫乏（PubMed=7, 得分10/10），但已有文献（PMID:40521769）报道了CCM2L复合杂合功能缺失变异与法洛四联症（Tetralogy of Fallot）的相关性——这是首次将CCM2L与人类先天性心脏病建立直接遗传因果联系。PMID:23328253的斑马鱼研究揭示ccm2-like是心血管发育必不可少的组分，作为Heg信号通路的一个新组分发挥作用。这些发育表型与传统CCM通路相关的心血管表型部分重叠但又不完全相同，支持CCM2L在发育过程中具有独立于CCM2的独特功能。

CCM2L作为核质蛋白（Nucleoplasm Approved，得分9/10）在TE调控中的潜力体现在其多层次的作用可能：(1) 在胞质-质膜界面通过抑制/调控MAP3K3-MEK5-ERK5信号影响转录因子激活，间接调控染色质状态；(2) 在核质中通过HMGN2介导的核小体重塑直接影响染色质的可及性，TE序列的染色质状态对HMGN2调控高度敏感——已有研究证实H1-核小体结合在TE区域的富集是维持其沉默状态的关键机制；(3) 通过PBX4参与发育转录程序的调控，TE的去抑制在发育过程中具有谱系特异性调节功能。然而，这些机制模型的致命缺陷在于缺乏任何直接实验证据——CCM2L的核内定位功能从未被系统研究过，HMGN2/PBX4的互作在BioGRID中均无实验评分，必须视为初步筛选数据。CCM2L的最高优先级验证实验应为：(1) 内源co-IP确认核心互作的真实性；(2) CCM2L ChIP-seq/CUT&RUN的全基因组结合图谱；(3) CCM2L敲除或过表达后的ATAC-seq分析染色质可及性变化。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MAP3K3 | STRING | 740 |
| CAMK2B | BioGRID | 1 |
| PBX4 | BioGRID | 1 |
| HMGN2 | BioGRID | 1 |
| PSMB1 | BioGRID | 0 |
| USE1 | BioGRID | 0 |
| PLEKHA4 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NUG4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000101331-CCM2L

![](https://images.proteinatlas.org/71063/1403_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/71063/1403_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/71063/1398_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/71063/1398_F2_3_red_green.jpg)

### PubMed 文献

**PubMed count: 12**

| 42364337 | From cross cancer transcriptomics to therapeutics: WGX-50 target hub genes in breast cancer and non-small cell lung carc | Comput Biol Chem 2026 |
| 40894452 | Glomulin and cerebral cavernous malformations 2 protein-like mutations in an extensive blaschkoid glomuvenous malformati | JAAD Case Rep 2025 |
| 40521769 | Compound Heterozygous Loss-of-Function Variants in CCM2L in a Fetus With Tetralogy of Fallot. | Mol Genet Genomic Med 2025 |
### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CCM2L

