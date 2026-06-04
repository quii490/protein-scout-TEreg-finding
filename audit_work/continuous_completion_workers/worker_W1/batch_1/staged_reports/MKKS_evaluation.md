---
type: protein-evaluation
gene: "MKKS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MKKS — REJECTED (研究热度过高 (PubMed strict=196，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MKKS / BBS6 |
| 蛋白名称 | Molecular chaperone MKKS |
| 蛋白大小 | 570 aa / 62.3 kDa |
| UniProt ID | Q9NPJ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centrosome, Basal body; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 10/10 | ×1 | 10 | 570 aa / 62.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=196 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002423, IPR027409, IPR027413, IPR028790, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome, Basal body | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- kinociliary basal body (GO:1902636)
- motile cilium (GO:0031514)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 196 |
| PubMed broad count | 255 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BBS6 |

**关键文献**:
1. Bardet-Biedl Syndrome Overview.. **. PMID: 20301537
2. Dual roles of the MPK3 and MPK6 mitogen-activated protein kinases in regulating Arabidopsis stomatal development.. *The Plant cell*. PMID: 39102898
3. Combining Cep290 and Mkks ciliopathy alleles in mice rescues sensory defects and restores ciliogenesis.. *The Journal of clinical investigation*. PMID: 22446187
4. Association between BBS6/MKKS gene polymorphisms, obesity and metabolic syndrome in the Greek population.. *International journal of obesity (2005)*. PMID: 18813213
5. MKKS is a centrosome-shuttling protein degraded by disease-causing mutations via CHIP-mediated ubiquitination.. *Molecular biology of the cell*. PMID: 18094050

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.0 |
| 高置信度残基 (pLDDT>90) 占比 | 64.6% |
| 置信残基 (pLDDT 70-90) 占比 | 26.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 0.7% |
| 有序区域 (pLDDT>70) 占比 | 91.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.0，有序区 91.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002423, IPR027409, IPR027413, IPR028790, IPR027410; Pfam: PF00118 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCT2 | 0.994 | 0.787 | — |
| CCT5 | 0.990 | 0.693 | — |
| CCT8 | 0.966 | 0.615 | — |
| BBS12 | 0.966 | 0.780 | — |
| CCT3 | 0.956 | 0.616 | — |
| CCT4 | 0.950 | 0.625 | — |
| BBS10 | 0.929 | 0.516 | — |
| TCP1 | 0.924 | 0.516 | — |
| CCT7 | 0.922 | 0.585 | — |
| HSPE1 | 0.798 | 0.470 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PTN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| STK16 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TGIF1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ICA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| deoB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| BBS7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22500027|imex:IM-17327 |
| TCP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22500027|imex:IM-17327 |
| CCT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22500027|imex:IM-17327 |
| BBS10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22500027|imex:IM-17327 |
| BBS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22500027|imex:IM-17327 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.0 + PDB: 无 | pLDDT=89.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Centrosome, Basal body | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MKKS — Molecular chaperone MKKS，研究基础较多，新颖性有限。
2. 蛋白大小570 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 196 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 196 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPJ1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125863-MKKS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MKKS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPJ1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
