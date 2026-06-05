---
type: protein-evaluation
gene: "HYPK"
date: 2026-06-01
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HYPK 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | HYPK / C15orf63 |
| 蛋白全名 | Huntingtin-interacting protein K |
| 蛋白大小 | 121 aa / 13.7 kDa |
| UniProt ID | Q9NX55 (HYPK_HUMAN) |
| 评估日期 | 2026-06-01 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 /1.83)

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | **24** | HPA: Nucleoplasm(Supported, 主定位)+Microtubules; GO: nucleoplasm(IDA:HPA)+nucleus(IDA); UniProt: Nucleus+Cytoplasm; 核质为主但胞质也有 |
| 蛋白大小 | 3/10 | ×1 | **3** | 121 aa / 13.7 kDa, 极小蛋白 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 39篇; ≤40区间 |
| 三维结构 | 8/10 | ×3 | **24** | PDB: 6C95(3.15A X-ray, 27-121)+6PW9(4.03A EM)+9F1D(3.26A EM); AF pLDDT 70.9; PDB+AF验证 |
| 调控结构域 | 5/10 | ×2 | **10** | HYPK/UBA-like domain; NatA复合体组分; N-terminal acetylation regulator |
| PPI | 5/10 | ×3 | **15** | STRING: NAA15(0.999)+NAA10(0.999)+NAA50(0.998)+HTT(0.986); IntAct: NAA15+NAA10+HTT+NAA50+MAGEA1; 核心NatA复合体 |
| 互证加分 | — | — | **+1.0** | PDB+AF双向验证; ≥2源NuLoc; IntAct+STRING共同确认核心PPI |
| **原始总分** | | | **117/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| HPA (IF) | Nucleoplasm (Supported, 主定位), Microtubules (附加) | Supported |
| UniProt | Nucleus; Cytoplasm | ECO:0000269 (实验) |
| GO-CC | nucleoplasm (IDA:HPA), nucleus (IDA:CAFA), cytoplasm (IDA:CAFA), microtubule cytoskeleton (IDA:HPA) | IDA |

**IF 图像**: HPA有IF展示图(3细胞系: A-431, U2OS, Hep-G2, NIH-3T3)，Nucleoplasm定位，Supported可靠性。

**结论**: HYPK的核定位由HPA IF(Supported, 主定位Nucleoplasm)和GO-CC实验证据(IDA)支持。UniProt实验证据确认Nucleus和Cytoplasm双重定位。作为NatA(N-terminal acetyltransferase complex A)的组分，HYPK的核质定位与N端乙酰化在核内的发生一致。但微管定位提示非核功能也存在。评分6分。

#### 3.2 蛋白大小评估
**评价**: 121 aa / 13.7 kDa，是极小的蛋白。远低于200-800 aa理想区间。小尺寸使其更适合作为伴侣/适配蛋白(如HYPK调节NatA活性的角色)。天然小蛋白也可能是优点(容易重组表达、结构解析更容易)。评分3分。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict | 39 |
| PubMed broad | 42 |
| Chromatin/epigenetics 比例 | ~15% |

**主要研究方向**:
- Huntingtin(HTT)互作与亨廷顿病
- NatA N-乙酰转移酶复合体的抑制/调节
- 分子伴侣活性(抑制polyQ蛋白聚集)
- 自噬中的多NEDD8化蛋白降解
- 核糖体NatA复合体动态交换(Nature 2024, Mol Cell 2025)

**关键文献**:
1. Lentzsch AM et al. (2024). "NAC guides a ribosomal multienzyme complex for nascent protein processing." *Nature*. PMID: 39169182
2. Lentzsch AM et al. (2025). "HYPK promotes N-terminal protein acetylation through rapid ribosome exchange of NatA." *Mol Cell*. PMID: 41380682
3. Firouzbakht A et al. (2024). "HYPK: A marginally disordered protein sensitive to charge decoration." *Proc Natl Acad Sci USA*. PMID: 38657047
4. Ghosh DK & Ranjan A (2022). "HYPK coordinates degradation of polyneddylated proteins by autophagy." *Autophagy*. PMID: 34836490
5. Szolajska E & Chroboczek J (2011). "Faithful chaperones." *Cell Mol Life Sci*. PMID: 21655914

**评价**: 39篇PubMed，高新颖性。HYPK的研究在2024-2025年出现爆发(Nature/Mol Cell/PNAS三篇高水平文章)，主要集中在核糖体-NatA复合体动态和N端乙酰化机制。Chromatin/epigenetics方向有内在关联(N端乙酰化影响蛋白质稳定性/定位/互作)，但HYPK本身不直接参与chromatin修饰。评分8分。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 70.9 |
| pLDDT >90 占比 | 27.3% |
| pLDDT 70-90 占比 | 29.8% |
| pLDDT 50-70 占比 | 27.3% |
| pLDDT <50 占比 | 15.7% |
| 可用 PDB 条目 | 3 (6C95/6PW9/9F1D) |

**PDB详情**:
- 6C95: X-ray 3.15A, 27-121, 与NAA15(TPR domain)复合物
- 6PW9: EM 4.03A, 全长(1-121), NatA(Naa10+Naa15+HYPK)复合物
- 9F1D: EM 3.26A, 全长(1-121), 核糖体-NatA复合物

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HYPK/HYPK-PAE.png]]

**评价**: 结构质量良好。3个PDB实验结构(包括X-ray和cryo-EM)，均在NatA/核糖体复合物背景下解析。HYPK作为"marginally disordered protein"(PMID:38657047)，折叠状态可能依赖于结合伴侣(NAA15/NAA10)。游离态部分无序但结合态折叠良好(conditional folding)。AlphaFold pLDDT=70.9，15.7%无序。评分8分。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| UniProt | 无 |
| InterPro | IPR052617 (HYPK family); IPR038922 (HYPK/UBA-like superfamily); IPR044034 (HYPK, UBA-like domain) |
| Pfam | PF19026 (HYPK_UBA) |

**调控潜力分析**: HYPK含UBA-like结构域，是NatA(Naa10+Naa15)复合体的核心调节亚基。HYPK通过与NAA15(TPR repeats)互作抑制NatA的N端乙酰转移酶活性，调控新生多肽的N-alpha乙酰化。N端乙酰化是最常见的蛋白质修饰之一(影响80%人类蛋白)，调控蛋白质稳定性、定位和互作。HYPK通过调控NatA间接影响包括chromatin蛋白在内的众多底物的乙酰化状态。此外，HYPK具有分子伴侣活性，可抑制polyQ-HTT聚集。但无直接DNA/chromatin结合活性。评分5分。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, 15条):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| NAA15 (Naa15) | TAP + Y2H array | 20360068/32296183 | NatA scaffold, TPR repeats | 间接(N端乙酰化) |
| NAA10 (Naa10) | TAP | 20360068 | NatA catalytic subunit | 间接(N端乙酰化) |
| Naa50 | anti tag coIP | 26496610 | NatE catalytic subunit | 间接(N端乙酰化) |
| Naa11 | anti tag coIP | 26496610 | NatA-like | 间接 |
| HTT | two hybrid | 17500595 | Huntingtin | 否(神经退行) |
| TSGA10IP | anti tag coIP | 28514442 | Testis-specific | 否 |
| MAGEA1 | validated Y2H | 25416956 | MAGE family, E3 regulator | 是(泛素化调控) |
| TXLNA | validated Y2H | 32296183 | Taxilin, vesicle trafficking | 否 |
| C2orf68 | Y2H array | 32296183 | Unknown | 未知 |
| KSR1 | anti tag coIP | 27086506 | Kinase scaffold | 信号传导 |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| NAA15 | 0.999 (exp 0.985) | NatA scaffold | 间接(乙酰化) |
| NAA10 | 0.999 (exp 0.978) | NatA catalytic | 间接(乙酰化) |
| NAA50 | 0.998 (exp 0.937) | NatE catalytic | 间接(乙酰化) |
| HTT | 0.986 (exp 0.62) | Huntingtin | 否 |
| NAA16 | 0.947 (exp 0.817) | NatA variant scaffold | 间接 |
| SRRT | 0.581 (exp 0.292) | Serrate, RNA processing | 间接(RNA) |
| ALPK2 | 0.597 (exp 0.597) | Alpha-kinase | 信号传导 |

**PPI 评价**: PPI网络以NatA/NatE乙酰转移酶复合体为核心(NAA15/NAA10/NAA50/NAA16/NAA11)。HTT互作反映分子伴侣功能。MAGEA1(Melanoma antigen family A1, E3泛素连接酶调节因子)的互作可能连接HYPK与泛素系统。N端乙酰化的广泛底物谱意味着HYPK间接影响大量chromatin蛋白(许多转录因子和chromatin修饰酶经历N端乙酰化)。但HYPK自身不与chromatin蛋白直接互作。评分5分。

### 4. 总体评价

**推荐等级**: 3星 (63.9/100)

**核心优势**:
1. 高新颖性(39篇)，2024-2025年Nature/Mol Cell/PNAS接连发表
2. PDB+EM三个结构(在NatA/核糖体复合物中)，结构信息丰富
3. N端乙酰化是影响~80%人类蛋白的普遍修饰，间接调控chromatin蛋白稳定性
4. 核定位多源确认(HPA IF Supported+GO+UniProt)
5. 分子伴侣活性(HTT)暗示多功能角色

**风险/不确定性**:
1. 蛋白极小(121aa)，自身结构域简单(UBA-like)
2. 主要功能为NatA调节亚基，非直接chromatin/DNA调控因子
3. Chromatin关联完全间接(通过N端乙酰化底物)
4. 15.7%无序区域，条件性折叠可能限制生化操作
5. HTT互作方向与TE调控无关

**下一步建议**:
- [ ] 鉴定核内HYPK-NatA复合体特异性的N端乙酰化底物(重点关注chromatin相关底物)
- [ ] 比较胞质NatA vs 核NatA的底物偏好差异
- [ ] 探究HYPK无序区域的磷酸化/修饰如何调控NatA活性和定位

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NX55
- Protein Atlas: https://www.proteinatlas.org/ENSG00000242028-HYPK
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HYPK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NX55
- STRING: https://string-db.org/ (HYPK)
- IntAct: https://www.ebi.ac.uk/intact/

**HPA IF 状态**: HPA IF 图像已本地嵌入。

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HYPK/IF_images/Hep-G2_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HYPK/IF_images/NIH-3T3_1.jpg]]。核定位基于HPA localization/reliability + UniProt + GO-CC。





#### PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| NAA15 | STRING | 0.999 |
| NAA10 | STRING | 0.999 |
| NAA50 | STRING | 0.998 |
| HTT | STRING | 0.986 |
| NAA16 | STRING | 0.947 |
| EIF1B | IntAct | psi-mi:"MI:0006"(anti bait coi |
| Naa15 | IntAct | psi-mi:"MI:0676"(tandem affini |
| Naa10 | IntAct | psi-mi:"MI:0676"(tandem affini |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HYPK/HYPK-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NX55-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
