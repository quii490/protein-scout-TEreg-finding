---
type: protein-evaluation
gene: "RCAN1"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RCAN1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | RCAN1 |
| 蛋白名称 | Calcipressin-1 (Down syndrome critical region protein 1) |
| 蛋白大小 | 252 aa / ~28 kDa |
| UniProt ID | P53805 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | 胞质: 钙调磷酸酶抑制因子, 主要胞质定位; 个别核内功能报道 |
| 蛋白大小 | 6/10 | ×1 | 6 | 252 aa |
| 研究新颖性 | 1/10 | ×5 | 5 | PubMed≈800+篇, 研究非常成熟 |
| 三维结构 | 6/10 | ×3 | 18 | NMR/PBD可用, 结构域折叠已明确 |
| 调控结构域 | 5/10 | ×2 | 10 | 钙调磷酸酶结合模体(PxIxIT) + SP重复磷酸化区域 |
| PPI 网络 | 4/10 | ×3 | 12 | PPI degree=11 |
| **加权总分** | | | **59/180** | |
| **归一化总分** | | | **32.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- calcineurin complex (GO:0005955)

**结论**: RCAN1主要在细胞质中与calcineurin A结合抑制其磷酸酶活性，虽有文献报道其可穿梭入核抑制NFAT信号，但主要定位仍在胞质。作为钙调磷酸酶抑制因子，主要功能空间非细胞核。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 252 aa，较小蛋白，适合NMR/晶体学研究。
- **研究现状**: PubMed超过800篇，唐氏综合征关键区域基因，研究极为成熟。
- **三维结构**: 多NMR/晶体结构可用，钙调磷酸酶结合界面已详细表征。
- **结构域**: PxIxIT钙调磷酸酶结合模体 + SP重复磷酸化区域 + C端抑制结构域。
- **PPI**: 11个互作配体(source STRING)，主要与calcineurin钙信号通路成员互作。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: RCAN1 — 钙调磷酸酶抑制因子(Calcipressin-1)，主要定位于细胞质，作为calcineurin信号通路关键调节因子。核定位证据不足，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P53805
- Protein Atlas: https://www.proteinatlas.org/search/RCAN1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RCAN1
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/RCAN1
