---
type: protein-evaluation
gene: "CGAS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CGAS — REJECTED (研究热度过高 (PubMed strict=2351，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CGAS / C6orf150, MB21D1 |
| 蛋白名称 | Cyclic GMP-AMP synthase |
| 蛋白大小 | 522 aa / 58.8 kDa |
| UniProt ID | Q8N884 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Cytosol; UniProt: Nucleus; Chromosome; Cell membrane; Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 522 aa / 58.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2351 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.8; PDB: 4KM5, 4LEV, 4LEW, 4MKP, 4O67, 4O68, 4O69 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR046903, IPR046906, IPR024810; Pfam: PF03281, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Cytosol | Supported |
| UniProt | Nucleus; Chromosome; Cell membrane; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- site of double-strand break (GO:0035861)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2351 |
| PubMed broad count | 6890 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf150, MB21D1 |

**关键文献**:
1. Cyclic GMP-AMP synthase is a cytosolic DNA sensor that activates the type I interferon pathway.. *Science (New York, N.Y.)*. PMID: 23258413
2. Mitochondria-localized cGAS suppresses ferroptosis to promote cancer progression.. *Cell research*. PMID: 36864172
3. MLKL activates the cGAS-STING pathway by releasing mitochondrial DNA upon necroptosis induction.. *Molecular cell*. PMID: 40614706
4. DNA sensing by the cGAS-STING pathway in health and disease.. *Nature reviews. Genetics*. PMID: 31358977
5. The cGAS-STING pathway activates transcription factor TFEB to stimulate lysosome biogenesis and pathogen clearance.. *Immunity*. PMID: 39689715

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.8 |
| 高置信度残基 (pLDDT>90) 占比 | 57.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 30.1% |
| 有序区域 (pLDDT>70) 占比 | 68.6% |
| 可用 PDB 条目 | 4KM5, 4LEV, 4LEW, 4MKP, 4O67, 4O68, 4O69, 5V8O, 5VDO, 5VDP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4KM5, 4LEV, 4LEW, 4MKP, 4O67, 4O68, 4O69, 5V8O, 5VDO, 5VDP）+ AlphaFold极高置信度预测（pLDDT=76.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046903, IPR046906, IPR024810; Pfam: PF03281, PF20266 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STING1 | 0.991 | 0.292 | — |
| BECN1 | 0.988 | 0.000 | — |
| H2AC20 | 0.950 | 0.905 | — |
| H2AC18 | 0.950 | 0.905 | — |
| TBK1 | 0.922 | 0.000 | — |
| IFI16 | 0.921 | 0.326 | — |
| H2BC12 | 0.913 | 0.905 | — |
| H2BC11 | 0.913 | 0.905 | — |
| H2AC4 | 0.906 | 0.905 | — |
| H2AC8 | 0.905 | 0.905 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ORF26 | psi-mi:"MI:0018"(two hybrid) | pubmed:18321973|imex:IM-12215 |
| ORF52 | psi-mi:"MI:0018"(two hybrid) | pubmed:18321973|imex:IM-12215 |
| ORF75 | psi-mi:"MI:0018"(two hybrid) | pubmed:18321973|imex:IM-12215 |
| ORF39 | psi-mi:"MI:0018"(two hybrid) | pubmed:18321973|imex:IM-12215 |
| ORF46 | psi-mi:"MI:0018"(two hybrid) | pubmed:18321973|imex:IM-12215 |
| ORF33 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18321973|imex:IM-12215 |
| KIE-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18321973|imex:IM-12215 |
| ORF53 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18321973|imex:IM-12215 |
| ENSMUSP00000063331.8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30135424|imex:IM-30182 |
| L0L2J9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30356214|imex:IM-30196 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.8 + PDB: 4KM5, 4LEV, 4LEW, 4MKP, 4O67,  | pLDDT=76.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Cell membrane; Cytoplasm, cyt / Nucleoplasm; 额外: Nuclear bodies, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CGAS — Cyclic GMP-AMP synthase，研究基础较多，新颖性有限。
2. 蛋白大小522 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2351 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2351 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N884
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164430-CGAS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CGAS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N884
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000164430-CGAS/subcellular

![](https://images.proteinatlas.org/31700/371_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/31700/371_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/31700/372_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/31700/372_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/31700/374_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/31700/374_G8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N884-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
