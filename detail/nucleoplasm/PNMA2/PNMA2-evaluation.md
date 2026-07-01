---
type: protein-evaluation
gene: "PNMA2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PNMA2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PNMA2 |
| 蛋白名称 | Paraneoplastic antigen Ma2 |
| 蛋白大小 | 364 aa / 41.5 kDa |
| UniProt ID | Q9UL42 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 364 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=17 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=81.0; PDB=1 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PNMA; PNMA_C; PNMA_N |
| PPI | 8/10 | ×3 | 24.0 | PPI degree=263 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **69.9/100** | 互证: +1 |

### 3. 分析
- HPA: nan (nan)
- PubMed: strict=17, broad=33
- AF pLDDT: 81.0 / PDB: 1
- InterPro: PNMA; PNMA_C; PNMA_N
- Pfam: PNMA; PNMA_N
- PPI degree=263 ChIP: None
38301645: PNMA2 forms immunogenic non-enveloped virus-like capsids associated with paraneo | 40323214: Unveiling the Role of PNMA2 in Endometriosis: From Proliferation and Apoptosis t | 35187673: Gag-like proteins: Novel mediators of prenatal alcohol exposure in neural develo

### 4. 总体评价
★★★★  **69.9/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Paraneoplastic antigen Ma2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR026523 |
| InterPro | IPR048270 |
| InterPro | IPR048271 |
| Pfam | PF14893 |
| Pfam | PF20846 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Paraneoplastic antigen Ma2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR026523 |
| InterPro | IPR048270 |
| InterPro | IPR048271 |
| Pfam | PF14893 |
| Pfam | PF20846 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DPYSL5 | STRING | 892 |
| BIN1 | STRING | 853 |
| ZIC4 | STRING | 838 |
| SOX1 | STRING | 745 |
| SLX4 | BioGRID | 1 |
| YWHAZ | BioGRID | 1 |
| PNMA1 | BioGRID | 1 |
| LATS2 | BioGRID | 1 |


### 深度机制分析

**结构域架构**：PNMA2（364 aa, 41.5 kDa, Q9UL42, Paraneoplastic antigen Ma2）是PNMA（paraneoplastic Ma antigen）家族成员——与Gag retroviral capsid蛋白的结构同源性极高。核心结构域：（1）PNMA_N域（IPR048271, Pfam PF20846, N-terminal domain）——与retroviral Gag MA（matrix）域在结构上同源——形成compact alpha-helical bundle（通常3-5个a-helix），功能上可能介导膜结合或蛋白多聚化的初始步骤；（2）PNMA域（IPR026523, Pfam PF14893）——与retroviral Gag CA（capsid）域同源——CA域在HIV-1 Gag中以CA N-terminal domain（NTD, beta-hairpin + cyclophilin A binding loop）和CA C-terminal domain（CTD, 4-helix bundle）组成，CA可自组装为hexameric和pentameric lattice以形成viral capsid core；（3）PNMA_C域（IPR048270）——C-terminal domain。AlphaFold pLDDT=81.0, PDB=1——结构可信度高。PMID:38301645的关键发现——PNMA2 forms immunogenic non-enveloped virus-like capsids——PNMA2自组装为二十面体病毒样颗粒（VLP），与retroviral Gag的capsid assembly过程惊人一致——Gag在质膜经MA域结合后再通过CA-CA interaction形成未成熟病毒粒子的hexameric lattice。PNMA2-encapsidated VLP不含核酸——但结构形态免疫原性足以触发抗Ma2自身免疫应答。

**PPI互作网络解读**：PPI degree=263——此批蛋白中最密集的PPI网络之一。DPYSL5（CRMP5/Collapsin response mediator protein 5, STRING 892）为细胞骨架调控因子——与PNMA2同为onconeuronal antigen（paraneoplastic neurological syndrome/PNS的自身抗体靶点）。BIN1（Bridging integrator 1/Amphiphysin 2, STRING 853）为BAR domain蛋白——参与膜曲率感知和T-tubule biogenesis——也是PNS自身抗原。ZIC4（STRING 838）和SOX1（STRING 745）为C2H2 zinc finger transcription factor和HMG-box transcription factor——均为神经发育关键TF和PNS抗原。PNMA1（paraneoplastic Ma antigen 1, BioGRID, score=1）为同家族成员——可能形成PNMA1-PNMA2 heteromeric VLP。LATS2（Large tumor suppressor kinase 2, BioGRID, score=1）为Hippo pathway核心激酶——YAP/TAZ phosphorylation→细胞质滞留和降解——肿瘤抑制因子。

**结构解读**：PNMA2的Gag-like fold是其机制核心。PNMA_N域（Gag MA-like）的N端通常含myristoylation signal (MGxxxS)——共翻译N-myristoylation后锚定至膜——PNMA2的N端序列类似含Gly2可经myristoylation——这可能是PNMA2 membrane association的机制。PNMA域（Gag CA-like）含有两个CA-like subdomain——CA NTD通过beta-hairpin和cyclophilin A binding loop与相邻CA分子的CTD互作→形成hexameric lattice——PNMA2可能类似地通过PNMA域间的CA-like interaction形成VLP六角形晶格。PMID:38301645中的cryo-EM结构很可能揭示了PNMA2 VLP的高分辨率结构——其中capsid类似T=1或T=3 icosahedral symmetry。

**机制模型**：（1）VLP形成和自身免疫——PNMA2在肿瘤（尤其是睾丸癌、乳腺癌、子宫内膜异位症）中异位表达——在肿瘤微环境中自组装为immunogenic non-enveloped VLP→经MHC-I/MHC-II cross-presentation→DC cell呈递PNMA2 antigens→CD8+ CTL和CD4+ Tfh activation→anti-Ma2 antibody-producing B cell clonal expansion→anti-Ma2 IgG穿越血脑屏障→与神经元表达的PNMA2 cross-react→paraneoplastic limbic encephalitis（边缘叶脑炎）和diencephalitis/brainstem encephalitis。（2）Hippo pathway调控（PMID:40323214子宫内膜异位症）——PNMA2在endometriosis中的高表达促进增殖和抑制凋亡——通过LATS2互作→可能抑制Hippo signaling→YAP/TAZ不被磷酸化→进入核内→TEAD-dependent transcription→促进增殖和抗凋亡基因（CTGF, CYR61, Survivin/BIRC5, c-Myc）表达。（3）Testicular germ cell tumor（TGCT）中Ma2抗原的异位表达驱动anti-Ma2 PNS——PNMA2在正常睾丸组织低表达，但TGCT中过表达——PNMA2-VLP可能通过IFN-I pathway激活innate immune signaling→增加肿瘤免疫原性——成为免疫治疗检查点抑制剂的预测性biomarker。

**TE调控展望**：PNMA2的Gag-like fold使其与TE调控产生独特联系。Retroviral Gag蛋白在ERV表达和病毒样颗粒形成中核心功能——PNMA2作为"domesticated Gag-like protein"代表了ERV Gag domain在进化中被宿主重新利用（exaptation）成细胞功能的案例——VLP形成能力保留但不再包装TE RNA。PNMA2-VLP在肿瘤中的immunogenicity↑→激活innate immune pathway（cGAS-STING, TLR7/8→IFN-I）→TE（ERV/LINE-1）的转录可能被broadly调控——IFN-I signaling已知激活或抑制TE转录（取决于TE类型和细胞context）。PNMA2 overexpression可能通过IFN response间接影响癌细胞中TE转录和dsRNA介导的viral mimicry——enhance anti-tumor immunity。LATS2-Hippo pathway的YAP/TAZ dependent TE transcription调控——TE DNA（尤其是ERVK LTR）可作为YAP/TAZ-TEAD的enhancer——PNMA2-LATS2互作调节Hippo活性→间接影响YAP/TAZ-dependent TE enhancer activity。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UL42-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 120**

| 42335446 | Isolated Peripheral Nervous System Presentation in Ma/Ma2-Associated Autoimmunity. | Neurol Neuroimmunol Neuroinflamm 2026 |
| 42146229 | Strain-Tunable Electronic and Optical Properties of KSnI(3) Perovskite Polymorphs: From Structural Stability to Optoelec | ACS Omega 2026 |
| 42029599 | Anti-Ma2 Paraneoplastic Encephalitis and Testicular Cancer: When the Hypothalamus Whispers-A Case Report and Systematic  | Med Sci (Basel) 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PNMA2

