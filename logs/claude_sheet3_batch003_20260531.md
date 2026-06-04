# Sheet3 batch003 执行日志

- **Time**: 2026-05-31 15:38–16:30 Asia/Shanghai
- **Supervisor**: Claude Code middle agent
- **Input genes**: AP5Z1, ADPRH, ARL4A, ARL6IP6, AARSD1
- **Excel source**: Sheet3 "研究很多", rows 12–16
- **Data packets**: `/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/{gene}.json`

## Harvest 状态摘要

所有 5 个 harvest packets 均 **全部 6 源 OK**（UniProt, AlphaFold, PubMed, STRING, IntAct, HPA）。无 DNS failure，无 URLError，无需重采。

## 结果

| # | Gene | Final class | Report path | Status | HPA IF status | PubMed strict/broad | PPI coverage |
|---|---|---|---|---|---|---|---|
| 1 | AP5Z1 | nucleus-cytoplasm | `detail/nucleus-cytoplasm/AP5Z1/AP5Z1-evaluation.md` | scored (72.1) | IF unavailable — HPA 仅 60x60 缩略图 | 18 / 24 | Strong AP-5 complex (STRING); NUP93 nuclear pore link (IntAct) |
| 2 | ADPRH | rejected | `detail/rejected/ADPRH/ADPRH-evaluation.md` | rejected | IF unavailable — HPA 仅 60x60 缩略图 | 6 / 7 | Weak, mostly textmining (STRING); limited two-hybrid (IntAct) |
| 3 | ARL4A | nucleolus | `detail/nucleolus/ARL4A/ARL4A-evaluation.md` | scored (79.5) | IF unavailable — HPA 仅 60x60 缩略图 | 17 / 33 | Strong (STRING); KPNA2 importin link; multi two-hybrid (IntAct) |
| 4 | ARL6IP6 | nuclear-envelope | `detail/nuclear-envelope/ARL6IP6/ARL6IP6-evaluation.md` | scored (55.2) | IF unavailable — HPA 仅 60x60 缩略图 | 7 / 10 | Weak (STRING textmining); TMEM protein two-hybrid (IntAct) |
| 5 | AARSD1 | rejected | `detail/rejected/AARSD1/AARSD1-evaluation.md` | rejected | IF unavailable — HPA 无 IF 图像（仅 IHC/cell/RNA 缩略图） | 8 / 13 | Moderate (STRING); ARID4B co-score; multi two-hybrid/LUMIER (IntAct) |

## 分类理由

### AP5Z1 → nucleus-cytoplasm
UniProt 实验级注释 Cytoplasm + Nucleus (ECO:0000269)。GO-CC 有 nuclear speck IDA:HPA, nucleoplasm IDA:HPA, nucleus IDA:UniProtKB，同时有 cytoplasm/late endosome/lysosome。DNA repair 功能注释 (PMID:20613862) 提供核功能依据。NUP93 核孔互作提示核质运输关联。主要功能背景为 AP-5 adaptor complex/endosomal transport，非经典核蛋白。**核定位分 6/10**，归一化 **72.1/100**。

### ADPRH → rejected
UniProt Subcellular Location 字段完全为空。GO-CC 仅有 extracellular space (IEA:Ensembl)，无任何核相关条目。功能为胞质/胞外 ADP-ribosylarginine hydrolase。尽管结构数据极优质（4 PDB, pLDDT 98.4）和极新颖 (strict=6)，无定位证据支持核分类。**核定位分 0/10**。

### ARL4A → nucleolus
UniProt 明确注释 "Nucleus, nucleolus"。GO-CC 有 nucleolus IDA:UniProtKB + nucleoplasm IDA:HPA + nucleus IDA:UniProtKB。多源实验证据强支持核仁定位。STRING 显示 KPNA2 (importin alpha-2) 互作，提供核输入通路线索。同时有膜/胞质功能（小 GTPase, CYTH 招募）。**核定位分 8/10**，归一化 **79.5/100**——本批最高分。

### ARL6IP6 → nuclear-envelope
UniProt 和 GO-CC 均注释 nuclear inner membrane，但证据均为序列相似性推断（ECO:0000250 / ISS），无实验验证。AlphaFold 预测高度无序（mean pLDDT 56.7, 35.4% <50）。PPI 以 TMEM/膜蛋白 two-hybrid 为主。**核定位分 4/10**（仅过阈值），归一化 **55.2/100**——low-confidence 核膜候选。

### AARSD1 → rejected
UniProt Subcellular Location 仅 Cytoplasm (ECO:0000250)。GO-CC nucleus 来自 HDA:UniProtKB（高通量直接 assay，可信度低于 IDA/IMP），与 UniProt 主定位矛盾。蛋白功能为胞质 tRNA 编辑（校正错误氨酰化的 tRNA(Ala)），无已知核功能。**核定位分 1/10**，不满足保留阈值。

## Gate 总览

| Metric | Value |
|---|---|
| Total processed (this batch) | 5 |
| Scored (nuclear) | 3 |
| Rejected | 2 |
| Harvest failures | 0/5 |
| Targeted strict validation | **0 errors, 0 warnings** |
| Full gate strict validation | **0 errors**, 402 historical warnings |
| Total scored | 1027 |
| Total eliminated | 984 |
| Grand total | 2011 |

## HPA IF 状态

本批 5 个蛋白 HPA 均仅返回 60x60 缩略图：
- **AP5Z1**: `if_selected_60x60.jpg` — 60x60 缩略图，非原图
- **ADPRH**: `if_selected_60x60.jpg` — 60x60 缩略图，非原图
- **ARL4A**: `if_selected_60x60.jpg` — 60x60 缩略图，非原图
- **ARL6IP6**: `if_selected_60x60.jpg` — 60x60 缩略图，非原图
- **AARSD1**: 检索到 IHC/cell/RNA 缩略图，**无 `if_` 前缀图像**

全部 5 个 **IF unavailable**。定位判断基于 UniProt + GO-CC。

## 缺失数据 / 注意事项

| Gene | 缺失项 | 影响 |
|---|---|---|
| AP5Z1 | PDB 无；PAE 图片未生成 | 结构评分基于 pLDDT 统计 |
| ADPRH | UniProt subcellular location 空 | 拒绝主因 |
| ARL4A | PDB 无；PAE 图片未生成 | 结构评分基于 pLDDT 统计 |
| ARL6IP6 | AlphaFold 极低置信度 (pLDDT 56.7)；无实验定位 | 核膜分类置信度低 |
| AARSD1 | HPA 无 IF 图像 | 拒绝因素之一 |

## 未解决 warning

本批 5 个基因 targeted validation **0 warnings**。全表 402 个历史 warnings 均非本批引入，与已存在的旧格式报告相关（PAE image absence notes 等），需后续批次逐步清理。

## 需要人工判断的问题

1. **ARL6IP6 核膜分类**: 该蛋白定位证据完全来自序列相似性推断 (ECO:0000250)，无任何实验验证。AlphaFold 预测高度无序 (pLDDT 56.7)。虽有 UniProt + GO 双源一致注释 "nuclear inner membrane"，但置信度极低。建议后续优先获取实验定位数据后重新评估是否保留。

2. **ARL4A 核仁 vs nucleus-cytoplasm**: UniProt 注释 "Nucleus, nucleolus"，但文献焦点几乎全在胞质/膜功能（细胞迁移、endosome、EGFR 信号）。核仁功能的独立研究缺乏。KPNA2 importin 互作提供了核输入的分子机制线索，但核仁功能是否真实存在需实验验证。

3. **AARSD1 的 GO nucleus HDA**: 唯一的核证据是 GO-CC nucleus (HDA:UniProtKB)。如果后续有文献或独立实验支持核定位，可重新评估。

4. **ADPRH**: 尽管 UniProt 无定位注释且 GO-CC 仅胞外空间，ADP-ribosylhydrolase 家族中 PARG 等成员有明确核定位。ADPRH 的结构数据极其优质（4 PDB + pLDDT 98.4），如果未来发现核定位证据，应重新考虑。
