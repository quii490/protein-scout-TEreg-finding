---
type: protein-evaluation
gene: "SKI"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SKI — REJECTED (研究热度过高 (PubMed strict=866，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SKI |
| 蛋白名称 | Ski oncogene |
| 蛋白大小 | 728 aa / 80.0 kDa |
| UniProt ID | P12755 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Golgi apparatus; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 728 aa / 80.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=866 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.7; PDB: 1MR1, 1SBX, 5XOD, 6ZVQ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR014890, IPR047315, IPR009061, IPR010919, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Golgi apparatus | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)
- protein-containing complex (GO:0032991)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 866 |
| PubMed broad count | 5617 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Synthetic lethality of mRNA quality control complexes in cancer.. *Nature*. PMID: 39910291
2. Network pharmacology-based study on the mechanism of ShenKang injection in diabetic kidney disease through Keap1/Nrf2/Ho-1 signaling pathway.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 37392674
3. Syndromic diarrhea/Tricho-hepato-enteric syndrome.. *Orphanet journal of rare diseases*. PMID: 23302111
4. An anti-FAP-scFv-functionalized exosome-carrying hydrogel delivers SKI mRNA to fibrotic nucleus pulposus cells to alleviate intervertebral disc degeneration by regulating FOXO3.. *Theranostics*. PMID: 40213661
5. SKI regulates rRNA transcription and pericentromeric heterochromatin to ensure centromere integrity and genome stability.. *Neoplasia (New York, N.Y.)*. PMID: 40609276

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.7 |
| 高置信度残基 (pLDDT>90) 占比 | 35.2% |
| 置信残基 (pLDDT 70-90) 占比 | 14.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.7% |
| 低置信 (pLDDT<50) 占比 | 42.3% |
| 有序区域 (pLDDT>70) 占比 | 50.0% |
| 可用 PDB 条目 | 1MR1, 1SBX, 5XOD, 6ZVQ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.7），有序残基占 50.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR014890, IPR047315, IPR009061, IPR010919, IPR003380; Pfam: PF08782, PF02437 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMAD4 | 0.998 | 0.994 | — |
| SMAD2 | 0.997 | 0.993 | — |
| SMAD3 | 0.983 | 0.947 | — |
| NCOR1 | 0.947 | 0.785 | — |
| SKIL | 0.916 | 0.828 | — |
| SMAD1 | 0.908 | 0.766 | — |
| RNF111 | 0.864 | 0.631 | — |
| SNW1 | 0.833 | 0.620 | — |
| SMAD5 | 0.821 | 0.559 | — |
| SIN3A | 0.777 | 0.735 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMAD4 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:12419246 |
| SMAD2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18729074|imex:IM-19222 |
| HRNR | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| hh | psi-mi:"MI:0045"(experimental interaction detectio | pubmed:unassigned4 |
| Dmel\CG13022 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Arp5 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| aas | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SMAD3 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:22442258|imex:IM-20987 |
| NLK | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| DYRK1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.7 + PDB: 1MR1, 1SBX, 5XOD, 6ZVQ | pLDDT=65.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear bodies, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SKI — Ski oncogene，研究基础较多，新颖性有限。
2. 蛋白大小728 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 866 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 866 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P12755
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157933-SKI/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SKI
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P12755
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
