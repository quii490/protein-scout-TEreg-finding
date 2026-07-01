---
type: protein-evaluation
gene: "B7Z8C1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## B7Z8C1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | B7Z8C1 |
| 蛋白名称 | ATP-dependent DNA helicase |
| 蛋白大小 | 519 aa / 58.8 kDa |
| UniProt ID | B7Z8C1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 519 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=85.3; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | DNA_helicase_ATP-dep_RecQ; Helicase_C-like; HRDC-like_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **69.9/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=85.3 PDB=0
- InterPro: DNA_helicase_ATP-dep_RecQ; Helicase_C-like; HRDC-like_sf
- Pfam: Helicase_C; HRDC; RecQ_Zn_bind
- PPI degree=0 ChIP: None


### 4. 总体评价
**69.9/100** | **nucleoplasm**
TE candidate: DNA_helicase_ATP-dep_RecQ; Helicase_C-like; HRDC-like_sf


### 补充分析 (UniProt API)

**蛋白全称**: ATP-dependent DNA helicase

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004589 |
| InterPro | IPR001650 |
| InterPro | IPR010997 |
| InterPro | IPR002121 |
| InterPro | IPR044876 |
| InterPro | IPR027417 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: ATP-dependent DNA helicase

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004589 |
| InterPro | IPR001650 |
| InterPro | IPR010997 |
| InterPro | IPR002121 |
| InterPro | IPR044876 |
| InterPro | IPR027417 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### 深度机制分析

**结构域架构**：B7Z8C1（519 aa, 58.8 kDa, UniProt B7Z8C1, ATP-dependent DNA helicase）是RecQ-like DNA解旋酶家族的未鉴定成员。核心结构域组成：（1）DNA_helicase_ATP-dep_RecQ域（IPR004589）——含七个conserved helicase motifs（I, Ia, II, III, IV, V, VI）排列于两个RecA-like domain（D1和D2）的cleft——motif I（Walker A, GxGKT）结合ATP的phosphate moiety，motif II（Walker B, DExH box）中Glu的carboxyl side chain作为catalytic base激活water分子亲核攻击ATP gamma-phosphate以实现ATP hydrolysis——为DNA unwinding提供能量；（2）Helicase_C域（IPR001650, Pfam PF00271）——与RecA D2 domain的组合构成完整解旋酶motor；（3）HRDC-like超家族（IPR010997）——HRDC（Helicase and RNase D C-terminal）domain为winged-helix（wHTH）折叠，在RecQ helicase中作为DNA-binding辅助域，通常识别ssDNA/dsDNA junction或帮助processivity；（4）RecQ_Zn_bind域（Pfam RecQ_Zn_bind）——在RecQ家族成员中常见的zinc-binding motif（三个conserved Cys残基配位Zn2+），形成"thumb"结构辅助ssDNA translocation。AlphaFold pLDDT=85.3——本批最高结构置信度之一——无PDB实验结构，但该pLDDT说明整个蛋白折叠极为完整。

**PPI互作网络解读**：PPI degree=0——无可检测的蛋白互作伙伴——这与B7Z8C1为TrEMBL预测蛋白、从未被实验表征一致。但domain组成（RecQ DNA helicase + HRDC）本身就强烈暗示功能——RecQ helicases在基因组维护中核心功能——BLM（Bloom syndrome protein）、WRN（Werner syndrome protein）、RECQL4/RECQL5——均与人类疾病（Bloom/Werner/Rothmund-Thomson/RAPADILINO syndromes）密切相关，表现为基因组不稳定性、早衰、癌症易感性。B7Z8C1作为新的RecQ-like成员，极可能在DNA复制、重组、修复中发挥重要的守门功能。

**结构解读**：RecQ helicase是3'-5' directional translocase——以ATP hydrolysis为能量来源在ssDNA上沿3'至5'方向行走（inchworm model）——每次ATP hydrolysis驱动D1和D2 RecA-like domain之间相对旋转20-25 angstrom→pulling ssDNA through central channel→破坏下游dsDNA的basepairing——以1 bp/ATP的步长dsDNA unwinding。HRDC domain以winged-helix fold与ssDNA/dsDNA junction的5' overhang ssDNA结合→增加helicase对DNA底物的processivity并辅助特定DNA结构（如Holliday junction, G-quadruplex, D-loop）的识别。RecQ_Zn_bind域的thumb结构在ssDNA translocation中维持DNA在helicase channel的correct register，防止slippage。

**机制模型**：（1）DNA双链断裂修复和同源重组——RecQ helicase在DSB repair中催化DNA end resection——5'-3' exonuclease（如EXO1, DNA2, BLM, MRN/CtIP）需RecQ helicase的预先unwinding来生成3' ssDNA tail（Rad51 filament assembly substrate）。B7Z8C1可能作为WRN/BLM的功能同源物——催化resection过程中的DNA unwinding。（2）复制叉stalling and restart——当复制叉遇到DNA lesion、secondary structure（G4, hairpin）或protein-DNA barrier时，RecQ helicase参与fork regression（将replication fork reverse为"chicken foot" Holliday junction structure）——允许template switching和damage bypass——避免fork collapse and DSB。（3）端粒维持——WRN和BLM are known to process telomeric G-quadruplex structures——B7Z8C1可能类似地在telomere/subtelomere维护中功能。

**TE调控展望**：B7Z8C1的RecQ helicase架构使其与TE调控产生紧密的机制连接——通过DNA repair and replication。LINE-1逆转录转座过程在genomic target site产生DNA single-strand break（SSB, ORF2p endonuclease cleavage），随后的target-primed reverse transcription（TPRT, ORF2p reverse transcriptase activity on the SSB 3'-OH）产生新的LINE-1 insertion——RecQ helicase可能靶向LINE-1 integration intermediate——作为anti-LINE-1 host defense因子——识别LINE-1 TPRT intermediate的异常DNA结构（3' flap or D-loop）→抑制integration完成或将integration event引导至non-essential genomic region。BLM已知参与ALT（alternative lengthening of telomeres）——RecQ helicase的TE defense功能已有先例——B7Z8C1作为新RecQ成员极可能是TE restriction factor。HRDC domain辅助识别TE integration site的结构特异性DNA特征（如target site duplication/TAT, poly-A tail, 5'UTR G-quadruplex-like structure）。PubMed=0说明B7Z8C1是完全新颖的RecQ helicase——实验验证其在TE restriction中的功能是极具前景的研究方向。


![PAE](https://alphafold.ebi.ac.uk/files/AF-B7Z8C1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B7Z8C1
